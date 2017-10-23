#-*- coding:utf-8 -*-
import jieba
import re
import ConfigParser

class Vector(object):

    def __init__(self, conf):
        self.conf = self._parser(conf)
        for 

    def _parser(self, fin):
        conf_dict = {}
        cf = ConfigParser.ConfigParser()
        cf.read(fin)
        
        for section in cf.sections():
            conf_dict.update({section:{}})
            for key, val in cf.items(section):
                conf_dict[section].update({key:val})
        return conf_dict
    

    def str2vec(self, st):
        if isinstance(st, unicode):
            st = st.decode("utf-8")
        st = re.sub(r'[^\u4e00-\u9fa5]', '', st)
        seg_list = jieba.cut(st, cut_all = False, HMM = True)
        return "\t".join(seg_list)


    
