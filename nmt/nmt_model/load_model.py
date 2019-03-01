#-*- coding:utf-8 -*-
import tensorflow as tf



def read_graph_from_ckpt(ckpt_path, input_names, output_name):
    """
    @brief: 从ckpt节点读取graph结构
    """
    saver = tf.train.import_meta_graph(ckpt_path + '.meta', clear_devices = True)
    graph = tf.get_default_graph()
    
    with tf.Session(graph = graph) as sess:
        sess.run(tf.global_variables_initializer())
        saver.restore(sess, ckpt_path)
        output_tf = graph.get_tensor_by_name(output_name)
        pb_graph = tf.graph_util.convert_variables_to_constants(sess, graph.as_graph_def(), [output_tf.op.name])
        

    with tf.Graph().as_default() as g:
        tf.import_graph_def(pb_graph, name='')
    
    with tf.Session(graph=g) as sess:
        OPS=get_ops_from_pb(g,input_names,output_name)
    return OPS
