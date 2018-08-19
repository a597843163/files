### 认识命令

#### 基础命令

pwd 打印所在⽬录
cd 打开对应的⽬录

../进⼊上次的⽬录

~ 和 /home/登录的⽤户⽬录
/ 根⽬录
ls 列出⽬录下⾯所有的⽂件
cat 查询命令
dd 创建⼀个500M⽂件
 dd if=“/dev/zero” of=“file_500M” bs=50M count=10
 输⼊⽂件 输出⽂件 块⼤⼩ 数量
sudo 临时提⾼权限
free -m m:MB k:KB g:GB
rm -rf 移除⽂件
tar -xvf 从gz解压
 -cvf 打包压缩成gz
copy ⽂件a 路径b
touch 创建简单txt⽂件

#### 1.⽇常操作

![日常](C:\Users\sdsd\Desktop\笔记\img\日常.jpg)

![日常2](C:\Users\sdsd\Desktop\笔记\img\日常2.jpg)

#### 2.Bash 快捷键

![快捷键](C:\Users\sdsd\Desktop\笔记\img\快捷键.jpg)

#### 3.权限管理

![权限管理](C:\Users\sdsd\Desktop\笔记\img\权限管理.jpg)

#### 4.登录状态

uname -a  查看全部硬件
hostname 查看/修改主机名
w 查看登陆者信息
who 查看登陆者信息
whoami 当前的⽤户名
last 最近登录记录

#### 5.⽇志管理

cat 文件名 查看⽂件 但是它是把全部内容加到内存中
head -n10 文件名 前10⾏
tail -n10 文件名 尾部10⾏
每⼀次使⽤less 命令的时候,⼤约会先加载2到3屏的数据
less / more 尽可能少/多的加载⽂件
 按j向下
 按k向上
 按f向下翻屏
 按b向上翻屏
 按g到全⽂开头
 按G到全⽂结尾 shift+g
 按q退出
sort 文件名  排序 | uniq 去重
awk ’{print $N}‘ 打印出每行的第N列(加逗号添加第N列)
wc 字符(-c)、单词(-w)、⾏(-l)的计数
history | awk ‘{print $4}’ | sort | uniq -c | sort -r | head -n 10

#### 6.下载相关

curl 执⾏HTTP访问,也可以⽤来下载
http:80 https:443 超⽂本传输协议 ssl,tsl
请求头: cookies 浏览器信息 语⾔
请求体: 表单提交 post请求,参数放在请求体,
请求⽅法: get请求 post请求 delete请求 put请求 he)d请求
⽹址: http:// www. baidu .com : 80 ? 参数=xxx #锚点
get请求
数据库接⼝ python/java : get请求 post请求 delete请求 put
请求
nodejs get请求 post请求
对应数据库就是 增删改查
wget 下载⽂件

#### 7.安装软件包

apt debain 系 linux 的程序安装
apt 源
apt update 更新软件信息,更新本地软件列表
apt upgrade 升级软件
apt search {soft_name} 查找软件
apt install {soft_name} 安装软件
apt remove {soft_name} 移除软件
apt list --upgradable
yum redhat 系 Linux 的程序安装
rpm 安装包
 yum install {soft_name}
源码安装 make 编译
 ./configure 配置编译
 make 执⾏编译
 make install 安装编译⽂件到系统⽬录
 make clean 删除编译结果

#### 8.远程登录

0~1024 1025~65535 10000以上
ssh -p 22120 192.168.143.132
ssh {username@host} 默认端⼝22,其他端⼝使⽤ -p 参数
 RSA Key
 ssh-keygen 创建⾃⼰的密钥对
 配置修改: /etc/ssh/ssh_config
 本地执⾏远程命令: ssh username@host ‘{command}’
SSH 服务端 : sshd
 配置修改: /etc/ssh/sshd_config
 重启服务: service ssh restart (旧)
 systemctl restart ssh (新)
 开机⾃动启动服务: service ssh enable(旧)
 systemctl enable ssh (新)
scp {filename} username@host:/path/

#### 9.压缩解压

tar
 -z, -j, -J, --lzm" Compress achive with gzip/bzip2/xz/lzm"
 压缩: tar -czf newfile.tar.gz dest_files gz bz2
 解压: tar -xzf file.tar.gz 	

-xjf file.bz2 zip

 压缩: zip -r newfile.zip src-file1 src-file2 … 多个⽂件压缩
 解压: unzip file.zip 

#### 10.grep查找相关

grep
 参数
 -i 忽略⼤⼩写
 -E 正则表达式匹配
 -rn 递归查找⽬录,并打印⾏号
 -include=‘*.py’  文件路径 仅包含.py结尾的⽂件
 -exclude=‘*.js’ 文件路径 不包含.js结尾的⽂件
find {file_dir} -name ‘*.xxxx’ 找到⽬录下所有名字匹配的⽂件
 找出⽂件夹 /tmp/xyz 下所有的权限为755 ,⼤⼩在 10k 到 100k
之间的log⽂件
 find /tmp/xyz -perm 0755 -size +10k -size -100k -name
‘*.log’
which 精确查找当前可执⾏的命令
whereis 查找所有匹配的命令

#### 11.⽹络管理

ifconfig 查看⽹卡状态
netstat -natp 查看⽹络连接状态
ping -i 0.5 {ip} 每隔0.5秒打印
lsof -i :{port} 查看占⽤的对应端⼝的程序
 lsof -i tcp 查看所有TCP连接
 lsof -u {username} 查看⽤户username 打开的所有⽂件
 lsof -p 查看pid为123的进程打开的所有⽂件
telnet {host_+ddress} {port} 查看远程主机的⽹络连接状态
traceroute {host_+ddress} 路由跟踪
dig {DOMAIN} DNS 查询

#### 12.⽂本处理⼯具

vim : 编译器之神
 esc 键,默认模式(浏览模式)
 ctl + e 向下滚动
 ctl + y 向上滚动
 ctl + f 向下翻屏
 ctl + b 向上翻屏

ctrl+v	列编辑模式

shift+v	行编辑模式

 yy 复制整⾏
 yw 复制后⾯⼀个单词 根据符号根据空格去间隔单词
 ⼩p 粘贴到下⼀⾏
 ⼤P 粘贴到上⼀⾏
 dd 删除整⾏
 d3w 向前删除3个单词
 c3w 剪切3个单词
 u 撤销操作
 ctl + r 重做
 gg 跳⾄⽂件⾸⾏
 shift + g 跳⾄⽂件结尾
 shift + h 跳⾄屏幕开头
 shift + m 跳⾄屏幕中间
 shift + l 跳⾄屏幕结尾
 i 键 , 插⼊模式
 : 键 , 命令模式
 :/需要搜索的⽂字
 set nu 打开⾏号
 set nonu 关闭⾏号
 23 跳⾄⽂件第23⾏
 w 保存
 q 退出
 wq 保存退出
 q! 强制关闭
ctl + v 列编辑
shift + v 选中整列
shift + > 向右缩进
shift + < 向左缩进

#### 13.磁盘管理

du -hs 查看⽂件或⽂件夹⼤⼩
df -h 查看磁盘分区的占⽤情况
fdisk -l 查看分区信息
dd 以块级别进⾏磁盘复制
 if (input file) 输⼊⽂件
 of (output file) 输出⽂件
 bs (blosk size) 块⼤⼩ (单位: K ,M ,G)
 count 块数量
 dd if=[src_file] of=[dst_file] bs=[size] count=[num]
 从iso⽂件制作启动U盘 dd if=/your_p>th/ubuntu.iso of=/dev/
disk3 bs=1m ![日常2](C:\Users\sdsd\Desktop\笔记\img\日常2.jpg)

### 操作实现

#### ssh远程访问服务器

需求:需要设备间通过ssh访问对⽅的⽂件⽬录系统
简单来说,就是从⼀台ubuntu电脑上,连接另外⼀台ubuntu电脑
shell
ssh 命令 secure sh 安全的shell
openssh-server ssh服务端
openssh-client ssh客户端

vim 编辑器 i:进⼊插⼊模式
保存退出 :wq
⾸先安装apt-get install vim openssh-server opensshclient
-y
1 vi服务端的/etc/ssh/sshd_config
把PasswordAuthentication设成yes
把#PermitRootLogin no改为PermitRootLogin yes
2 重启服务器端的sshd服务
service ssh restart
systemctl restart ssh
 /etc/init.d/ssh restart
apt ubuntu的命令
apt install 安装 XXXXXX
tree -L 等级 树形⽂件⽬录结构



#### 修改电脑名字

修改电脑名字,改完后重启终端或者,su ⼀下就更新完成
hostnamectl set-hostname xxxxxxx

#### 配置公钥给电脑

公钥 私钥
public private
成对存在,A电脑⽣成公钥和私钥后,把公钥分发到B电脑,
B电脑拿着公钥去访问A电脑,A电脑通过私钥去匹配公钥是
否匹对,如果正确就会给B电脑链接上A电脑从A电脑把内容拷⻉到B电脑上
免密码登录,需求相互登录的时候,不需要输⼊密码
ssh-keygen	生成公钥
ssh-keygen把⽣成的公私钥放在 /root/.ssh/id_rsa 加密
短语,短语越⻓加密效果越好

 ssh-copy-id 192.168.143.131	把此电脑公钥拷贝到B电脑

#### 软硬连接

ln link
软链接 ln -s source_file(全路径) dest_filepath(全路径)
硬链接 ln source_file dest_filepath

#### 修改权限

r 读操作 w 写操作 x执⾏操作
⽂件格式 所属⽤户的读写执⾏ 所属组成员对⽂件
的读写执⾏ 其他组成员对⽂件的读写执⾏操作![363003_1227493859FdXT](C:\Users\sdsd\Desktop\363003_1227493859FdXT.png)

修改方式1：chmod	777（二进制）   文件名

​	2：chmod	 u（user）=rwx,g（group）=rx,o（others）=r  文件名

​		chmod  a-x test1  所有的去掉x写权限

#### 为系统加硬盘

为linux系统加硬盘
1.在购买增加的硬盘⼤⼩
2.打开服务器,在我们的终端输⼊ fdisk /dev/sda
3.输⼊n , 增加⼀个 primary 分区 (输⼊ p)

4.为硬盘分区加⼤⼩空间

![1](C:\Users\sdsd\Desktop\笔记\img\QQ截图20180412193128.jpg)

5.输⼊w退出

输⼊命令刷新sda
partprobe /dev/sda
partx /dev/sda

![QQ截图20180412193128](C:\Users\sdsd\Desktop\笔记\img\QQ截图20180412193128.jpg)

6.输⼊ mkfs.ext4 /dev/sda3 格式化分区

7.创建⽂件挂载 mkdir /mnt/sd_new
mount /dev/sd3 /mnt/sd_new
8.查看是否挂载上 df -h





### 