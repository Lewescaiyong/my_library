#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import time
import socket
import paramiko
from threading import Event


class SSHConnection(object):
    """
    类名:       SSHConnection
    功能描述:   SSH连接类
    输入参数:   connect_info        type(dict)         设备连接信息
               --------------------------------------------------
               connect_info字典键值对信息
               ip                  type(str)           ip地址
               user                type(str)           登录用户名
               pass_word           type(str)           登录密码
               port                type(str)           连接端口号
    输出结果:   conn: 网络连接对象
    调用样例:   connect_info = {'ip': '127.127.0.1', 'user': 'admin', 'password': '123456', 'port': 22}
               conn = SSHConnection(connect_info)
               conn.login()
    作者:
    创建时间:
    更新说明:
    """

    def __init__(self, connect_info):
        self.ip = connect_info['ip']
        self.user = connect_info['user']
        self.password = connect_info['password']
        self.port = connect_info.get('port', 22)
        self.trans = None
        self.channel = None
        self.sep = '\n'

    def login(self):
        """
        方法名称:   login
        功能描述:   登录设备
        输入参数:
        输出结果:
        调用样例:
        作者:
        创建时间:
        更新说明:
        """
        if not self.trans:
            self.trans = self.create_client()
        if not self.trans.is_authenticated():
            self.authentication()
        # 打开通道
        channel = self.trans.open_session()
        # 获取终端
        channel.get_pty(width=200, height=200)
        # 激活终端
        channel.invoke_shell()
        # 设置channel接收回显超时时间
        channel.settimeout(2)
        self.channel = channel
        # 登录状态检查
        self.login_analyze()

    def create_client(self):
        """
        方法名称:   create_client
        功能描述:   创建socket对象
        输入参数:
        输出结果:
        调用样例:
        作者:
        创建时间:
        更新说明:
        """
        for i in range(3):
            event = Event()
            # 创建socket
            trans = paramiko.Transport((self.ip, self.port))
            try:
                # 启动客户端
                trans.start_client(event=event)
                event.wait(10)
                if not event.is_set():
                    raise paramiko.SSHException('create client timeout, ip: %s, port: %s.' % (
                        self.ip, self.port))
                if not trans.is_active():
                    raise paramiko.SSHException('create client failed, ip: %s, port: %s.' % (
                        self.ip, self.port))
            except (socket.timeout, socket.error, paramiko.SSHException) as e:
                print(e.message)
                trans.close()
                time.sleep(5)
            else:
                return trans
        # 抛出最近捕捉的异常
        raise

    def authentication(self):
        """
        方法名称:   authentication
        功能描述:   登录鉴权
        输入参数:
        输出结果:
        调用样例:
        作者:
        创建时间:
        更新说明:
        """
        if self.password:
            self.authentication_by_password()

    def authentication_by_password(self):
        """
        方法名称:   authentication_by_password
        功能描述:   使用用户名密码进行登录鉴权
        输入参数:
        输出结果:
        调用样例:
        作者:
        创建时间:
        更新说明:
        """
        event = Event()
        self.trans.auth_password(self.user, self.password, event)
        event.wait(10)
        if not event.set():
            raise paramiko.SSHException('auth_password timeout, user: %s, password: %s.' % (
                self.ip, self.port))
        if not self.trans.is_authenticated():
            error = self.trans.get_exception()
            if not error:
                error = paramiko.SSHException('auth_password failed, user: %s, password: %s.' % (
                    self.ip, self.port))
            raise error

    def login_analyze(self):
        """
        方法名称:   login_analyze
        功能描述:   登录状态分析
        输入参数:
        输出结果:
        调用样例:
        作者:
        创建时间:
        更新说明:
        """

    def close(self):
        """
        方法名称:   close
        功能描述:   退出登录
        输入参数:
        输出结果:
        调用样例:
        作者:
        创建时间:
        更新说明:
        """
        if self.trans:
            if self.channel:
                self.channel.close()
            self.trans.close()

        self.channel = None
        self.trans = None

    def reconnect(self):
        """
        方法名称:   reconnect
        功能描述:   重新建立连接
        输入参数:
        输出结果:
        调用样例:
        作者:
        创建时间:
        更新说明:
        """
        self.close()
        self.login()

    def cmd(self, cmd_info):
        """
        方法名称:   cmd
        功能描述:   命令下发接口
        输入参数:   cmd_info          type(dict)          需要下发的命令信息
                   --------------------------------------------------
                   cmd_info字典键值对信息
                   command             type(str)           需要下发的命令字符串
                   wait_str            type(str)           命令下发结束标志符
                   directory           type(str)           命令执行路径
                   input_list          type(list)          后续命令[cmd1, wait_str1, cmd2, wait_str2, ...]
                   input_dict          type(dict)          后续命令{cmd1: wait_str1, cmd2: wait_str2, ...}
                   timeout             type(int)           命令下发与回显接收超时时间
                   confirm             type(bool)          是否自动下发y/yes
        输出结果:   result = {'stdout': info after execute cmd}
        调用样例:   cmd_info = {'command': 'ls', 'wait_str': '#'}
                   result = conn.cmd(cmd_info)
        作者:
        创建时间:
        更新说明:
        """
        result = {'stdout': ''}

        # 判断是否需要切换工作路径
        if cmd_info.get('directory'):
            self.execute(command='cd %s' % cmd_info.get('directory'), wait_str='#')
        # 获取默认wait_str
        default_wait_str = [self.get_default_wait_str()]
        # 判断是否需要自动下发y/yes
        confirm = cmd_info.get('confirm', True)
        # 获取命令下发与回显接收超时时间
        timeout = cmd_info.get('timeout', 120)
        # 汇总需要下发的命令
        commands = [(cmd_info['command'], cmd_info.get('wait_str') or default_wait_str)]
        if cmd_info.get('input_list'):
            input_list = cmd_info['input_list']
            for i in range(len(input_list), 2):
                if i == len(input_list) - 1:
                    commands.append((input_list[i], default_wait_str))
                else:
                    commands.append((input_list[i], input_list[i + 1]))
        # 下发命令
        if cmd_info.get('input_dict'):
            input_dict = cmd_info['input_dict']
            wait_str = str(commands[0][1]) + '|' + '|'.join(input_dict.keys())
            info, is_match, match_str = self._cmd(commands[0][0], wait_str, timeout, confirm)
            while is_match and input_dict.get(match_str):
                result['stdout'] += info
                info, is_match, match_str = self._cmd(input_dict[match_str], wait_str, timeout, confirm)
            result['stdout'] += info
        else:
            for c, w in commands:
                info, is_match, match_str = self._cmd(c, w, timeout, confirm)
                result['stdout'] += info

        return result

    def _cmd(self, command, wait_str='#', timeout=120, confirm=True):
        """
        方法名称:   _cmd
        功能描述:   处理单个命令下发遇到y/n|yes/no回显的情况
        输入参数:   command             type(str)           需要下发的命令字符串
                   wait_str            type(str)           命令下发结束标志符
                   timeout             type(int)           命令下发与回显接收超时时间
                   confirm             type(bool)          是否自动下发y/yes
        输出结果:   info, is_match, match_str = receive_info, True, '#'
        调用样例:   info, is_match, match_str = conn._cmd('ls')
        作者:
        创建时间:
        更新说明:
        """
        all_info = ''
        if confirm:
            wait_str += '|y/n|yes/no'
        info, is_match, match_str = self.execute(command, wait_str, timeout)
        while match_str == 'y/n' and confirm:
            all_info += info
            info, is_match, match_str = self.execute('y', wait_str, timeout)
        while match_str == 'yes/no' and confirm:
            all_info += info
            info, is_match, match_str = self.execute('yes', wait_str, timeout)

        all_info += info

        return info, is_match, match_str

    def execute(self, command, wait_str='#', timeout=120):
        """
        方法名称:   execute
        功能描述:   单个命令下发、回显接收接口
        输入参数:   command             type(str)           需要下发的命令字符串
                   wait_str            type(str)           命令下发结束标志符
                   timeout             type(int)           命令下发与回显接收超时时间
        输出结果:   info, is_match, match_str = receive_info, True, '#'
        调用样例:   info, is_match, match_str = conn.execute('ls')
        作者:
        创建时间:
        更新说明:
        """
        if not self.send(command, timeout):
            return None, None, None

        info, is_match, match_str = self.receive(wait_str, timeout)

        return info, is_match, match_str

    def send(self, command, timeout=120):
        """
        方法名称:   send
        功能描述:   单个命令下发接口
        输入参数:   command             type(str)           需要下发的命令字符串
                   timeout             type(int)           命令下发与回显接收超时时间
        输出结果:   result = True or False
        调用样例:   result = conn.send('ls')
        作者:
        创建时间:
        更新说明:
        """
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                self.channel.send(command + self.sep)
                print('send cmd: [%s].' % command)
            except socket.timeout:
                print('send cmd: [%s] timeout.' % command)
                time.sleep(2)
            else:
                return True

        return False

    def receive(self, wait_str='#', timeout=120):
        """
        方法名称:   receive
        功能描述:   单个命令回显接收接口
        输入参数:   wait_str            type(str)           命令下发结束标志符
                   timeout             type(int)           命令下发与回显接收超时时间
        输出结果:   info, is_match, match_str = receive_info, True, '#'
        调用样例:   info, is_match, match_str = conn.receive('#')
        作者:
        创建时间:
        更新说明:
        """
        info = ''
        is_match = False
        match_str = None
        end_time = time.time() + timeout
        while time.time() < end_time:
            receive = ''
            try:
                receive = self.channel.recv(None)
            except socket.timeout:
                pass
            if receive:
                info += receive
            searcher = re.search(wait_str, receive)
            if searcher:
                is_match = True
                match_str = searcher.group()
                break
        # 剔除颜色字符
        info = re.sub(r'\x1b\[(?:\d{1,2};)?\d{0,2}m|\x1b\]\d{1,2};', '', info)
        print(info)

        return info, is_match, match_str

    def get_default_wait_str(self):
        """
        方法名称:   get_default_wait_str
        功能描述:   获取默认wait_str
        输入参数:
        输出结果:
        调用样例:
        作者:
        创建时间:
        更新说明:
        """

        return '#'

    def is_active(self):
        """
        方法名称:   is_active
        功能描述:   判断连接是否正常
        输入参数:
        输出结果:
        调用样例:
        作者:
        创建时间:
        更新说明:
        """

        if self.channel:
            return not self.channel.closed

        return False
