### APP功能：提供身份认证公共库。
### 开发人员：汪浩浩（whh881114@gmail.com）
### 更新日志：

### 修订日期：2019/06/08
1. 将原先的customized_authentication.py文件改名为my_authentication.py，原来的名称太长了，新建这个文件用于改写认证过程，不允许匿名用户访问。
2. 将原先的customized_permissions.py文件改为my_permissions包，在包中定义各种数据表的CURD权限。
3. 将原来的密码本的权限细分，具体如下。
    4. 主机权限依然保持一个总类，即host_perms.py来控制。
    4. 数据库权限细分为oracle和mysql，如果后续有postgresql，那么可以模向扩展，使用oracle_perms.py和mysql_perms.py控制。
    4. 网络设备先分为Cisco和h3c交换机类型，分别由cisco_perms.py和h3c_perms.py控制。
    4. 桌面类的依然不分类，使用helpdesk.py控制。


### 开发日期：2019/05/06
1. 功能列表：
    2. 登录功能。
    2. 登出功能。
    2. 验证用户登录状态。
    2. 验证用户密码不能为初始密码，并要按要求修改成复杂密码。