RNN 常见的使用方式见 LSTM 小节
在使用 tf.nn.dynamic_rnn 动态 RNN 时，为了获取最后时刻，也就是最后一个 cell 的输出，
通常对结果进行转置，把 time_step 放到第一维后取出
outputs = tf.transpose(outputs,[1,0,...]) '''转置 batch_size 和 time_step 维'''
pred = tf.contrib.layers.fully_connected(outputs[-1],n_classes,activation_fn = None)
 
tf.nn.static_rnn 则不具备 dynamic_rnn 这种自动补零的功能，并且它的输入是一个 list，代表时间序列
所以 tf.nn.static_rnn 通常搭配矩阵分解 tf.unstack() 一起使用。
X1 = tf.unstack(X,axis = 1)
outputs,_ = tf.nn.static_rnn(cell,X1,forget_bias = 1.0)
 
----------------------------------------------------------------------------
RNN dropout 功能示例
lstm_cell = tf.nn.rnn_cell.BasicLSTM(size,forget_bias = 0.0,state_is_tuple = True)
lstm_cell = tf.nn.rnn_cell.DropoutWrapper(lstm_cell,output_keep_prob = 0.5)
 
损失函数，关于 CTC 网络的 loss 就不能用均方差或者交叉熵来表示了，在TensorFlow 中封装了一个 ctc_loss 函数
tf.nn.ctc_loss(labels,inputs,sequence_length,time_major)
labels:一个 int32 类型的稀疏矩阵张量
inputs:当 time_major 为False 时形状为 [batch_size,max_time,num_lasses] ,否则 [max_time,batch_size,num_classes]
sequence_length: 序列长度
 
生成稀疏矩阵，密集矩阵就是我们常见的矩阵。当密集矩阵中大部分数据都为 0 时，就可以使用稀疏矩阵的方式来存储，指定 indices 和 value
indices 代表不为零的位置，value 代表对应的值，以及原来密集矩阵的形状 shape 。
tf.SparseTensor(indices = indices,value = value,shape = shape)
=> 稀疏转密集如下
tf.sparse_tensor_to_dense(sp_input,default = 0)
sp_input:一个 SparseTensor
default:默认值
 
利用稀疏矩阵计算编辑距离
def edit_distance(hypothesis,truth,normalize = True,name = "edit_distance")
hypothesis: SparseTensor 类型，输入预测的序列结果
truth: SparseTensor 类型，输入真实的序列结果
normalize: 默认为 True，求出来的编辑距离除以真实序列的长度
返回值: N-1 维的密集矩阵，包含每个序列的编辑距离
