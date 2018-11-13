# 分布式 TensorFlow
ps : 作为分布式训练的服务端，等待各个终端 supervisors 来连接
worker : 在 TensorFlow 的代码注释中被称为 supervisors ，作为分布式训练的运算终端
chief supervisors: 在众多运算终端中必须选择一个作为主要的运算终端，该终端是最先启动的。
 
# 定义 IP 和端口
strps_hosts = "localhost:1681"
strworker_hosts = "localhost:1682,localhost:1683"
 
# 定义角色名称
strjob_name = "ps"
task_index = 0
# 将字符转成数组
ps_hosts = strps_hosts.split(",")
worker_hosts = strworker_hosts.split(",")
 
# 创建 server
cluster_spec = tf.train.ClusterSpec({'ps':ps_hosts,'worker':worker_hosts})
server = tf.train.Server(
                    {'ps':ps_hosts,'worker':worker_hosts},
                    job_name = strjob_name,
                    task_index = task_index)
 
# 为ps 角色使用 join 等待
if strjob_name == 'ps':
    print "Wait"
    server.join()
    
在 tf.train.replica_device_setter 中使用 worker_device 来定义具体任务名称，使用 cluster 指定角色和对应的 IP 地址
with tf.device(tf.train.replica_device_setter(
        worker_device = "/job:worker/task:%d" % task_index,
        cluster = cluster_spec)):
    X = tf.placeholder("float")
    Y = tf.placeholder("float")
    W = tf.Variable(tf.random_normal([1]),name = "weight")
    b = tf.Variable(tf.zeros([1]),name = "bias")
    
    # 获得迭代次数
    global_step = tf.train.get_or_create_global_step()
    z = tf.multiply(X,W) + b
    cost = tf.reduce_mean(tf.square(Y - z))
    train_op = tf.train.GradientDescentOptimizer(0.01).minimize(cost,global_step = global_step)
    saver = tf.train.Saver(max_to_keep = 1)
    init = tf.global_variables_initializer()
    
    trainning_epochs = 2200
    display_step = 2
    # 设置主运算终端
    sv = tf.train.Supervisor(is_chief = (task_index == 0), # 0 号 worker 为 chief
                                logdir = "log/super/",
                                init_op = init,
                                saver = saver,
                                global_step = global_step,
                                save_model_secs = 5)
    # 连接目标角色 session
    with sv.managed_session(server.target) as sess:
        print global_step.eval(session = sess)
        for epoch in range(global_step.eval(session = sess),trainning_epochs * len(train_X)):
            for (x,y) in zip (train_X,train_Y):
                _,epoch = sess.run([train_op,global_step],feed_dict = {X:x,Y:y})
                ... 训练代码
        
        print "Finished"
        sv.saver.save(sess,"xxx" + "sv.cpk",global_step = epoch)
    
    sv.stop()
