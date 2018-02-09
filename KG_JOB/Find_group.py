#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from igraph import Graph as IGraph
from igraph import GraphBase
import igraph
class Find_Group():
    def __init__(self):
        # 初始参数设置
        self.min_group_capital = 50000000  # 集团注册资金最小值
        self.min_investment_capital = 10000000  # 集团投资企业注册资金最小值
        self.min_total_capital = 100000000  # 集团公司与投资企业注册资金最小总和
        self.min_investment_num = 5  # 集团投资企业最小个数
        self.ent_share_flag = True  # False:Share_ID->Ent_ID,True:Ent_ID->Share_ID
        self.min_share_num = 20  # 集团投资企业投资比例最小阈值
        self.max_share_num = 50  # 集团投资企业投资比例最大阈值
        self.group_indegree = 0  # 集团公司入度指标
        self.group_outdegree = 11 # 集团公司出度指标
        self.max_controllers_num = 300 # 最大控制人数量
    def search_final_group_root(self,KG,node_information_list,company_white_list,organization_type_list):# 寻找最终根节点
        node_capital={}
        company_information = {}
        for i in node_information_list:
            key = i[0]
            value = int(i[2])
            node_capital.setdefault(key, value)
        for j in node_information_list:
            key = j[1]
            value = j[0]
            company_information.setdefault(key, value)

        list1 = self.find_group_by_network(company_information,company_white_list)
        list2 = self.find_group_by_degree(KG)
        list3 = self.find_group_by_shares(KG)
        list4 = self.find_group_by_capital(KG,node_capital)
        # list5 = self.find_group_by_character(company_information,organization_type_list)
        group_lists=[list1,list2,list3,list4]
        group_list = self.search_group_root(KG,self.combining_group_lists(group_lists))
        return group_list

    def find_group_by_capital(self,KG,node_capital): # 使用注册资金规则来确立集团公司
        # KG为投资图谱
        # node_information:节点注册资金信息，使用字典储存{“ID”:“capital”}
        # 规则如下：
        # 1.待定企业注册资金大于5000万（可调值）
        # 2.待定企业向外有5家（可调值）以上的投资企业
        # 3.每一家投资企业注册资金在1000万（可调值）以上
        # 注册资金大于5000万的企业集合
        group_list = []
        for node in KG.vs:
            if node['name'] in node_capital.keys():
                if node_capital[node['name']] > self.min_group_capital:
                    group_list.append(node['name'])
        # 注册资金大于5000万但不符合以下规则：
            # 1.必须向外有5家以上的投资企业
            # 2.每家企业注册资金需要在1000万以上
        del_list = []
        for node in group_list:
            next_nodes = KG.vs[KG.neighbors(node, mode='out')]
            if len(next_nodes) < self.min_investment_num:
                del_list.append(node)
            else:
                # for min_node in next_nodes:
                #     if node_information[min_node['name']] < self.min_investment_capital:
                #         del_list.append(node)
                total_capital=node_capital[node['name']]
                for min_node in next_nodes:
                    total_capital+=node_capital[min_node['name']]
                if total_capital<self.min_total_capital:
                    del_list.append(node)
        for i in del_list:
            group_list.remove(i)
        # 返回最终识别的集团公司
        return group_list

    def find_group_by_network(self,company_information,company_white_list):# 根据企业白名单匹配
        # company_information:待匹配的企业信息 使用字典储存{“公司name”:“公司ID”}
        # company_white_list :企业白名单
        group_list = []
        for companyName in company_white_list:
            if companyName in company_information.keys():
                group_list.append(company_information[companyName])
        # 返回最终识别的集团公司
        return group_list

    def find_group_by_shares(self,KG):# 根据投资比例识别集团
        group_head = []
        group_list=[]
        for galaxy_circle in KG.vs:
            if self.ent_share_flag == False:
                next_nodes = KG.vs[KG.neighbors(galaxy_circle, mode='in')]
            else:
                next_nodes = KG.vs[KG.neighbors(galaxy_circle, mode='out')]
            next_nodes = [node['name'] for node in next_nodes if KG[galaxy_circle, node] > 50]
            if len(next_nodes) >= 3:
                group_head.append(galaxy_circle)
        # 确定集团母公司
        group_head_remove = []
        for mid_head in group_head:
            if self.ent_share_flag == False:
                next_nodes = KG.vs[KG.neighbors(mid_head, mode='out')]
            else:
                next_nodes = KG.vs[KG.neighbors(mid_head, mode='in')]
            if len(next_nodes) > 0:
                investment_max = max([KG[mid_head, node] for node in next_nodes])
            else:
                continue
            if investment_max > 50:
                next_node = [next_node['name'] for next_node in next_nodes if
                             KG.es[KG.get_eid(mid_head, next_node)]['weight'] == investment_max]
                if next_node[0] in group_head:
                    group_head_remove.append(mid_head)
        for i in group_head_remove:
            group_head.remove(i)
        for i in group_head:
            group_list.append(i['name'])
        return group_list

    # def find_group_by_shares(self, KG):  # 根据投资比例识别集团
    #     group_list = []
    #     client_group = []
    #     for temp_node in KG.vs:
    #         if self.ent_share_flag == False:
    #             next_nodes = KG.vs[KG.neighbors(temp_node, mode='in')]
    #         else:
    #             next_nodes = KG.vs[KG.neighbors(temp_node, mode='out')]
    #         for node in next_nodes:
    #             if len(next_nodes) > 0:
    #                 if KG[node, temp_node] >= self.max_share_num:
    #                     group_list.append(node['name'])
    #                 elif KG[node, temp_node]>= self.min_share_num and KG[node, temp_node]< self.max_share_num:
    #                     investment_max = max([KG[node, temp_node] for node in next_nodes])
    #                     group_node = [next_node['name'] for next_node in next_nodes if KG.es[KG.get_eid(node, temp_node)]['weight'] == investment_max]
    #                     group_list.append(group_node['name'])
    #             else:
    #                 continue
    #
    #     group_list = list(set(group_list))
    #     return group_list

    def find_group_by_controllers(self,KG): # 根据频繁控制人算法进行匹配
        top_node = []
        used_top_node=[]
        true_top_company=[]
        for node in KG.vs:
            if KG.indegree(node)==0:
                top_node.append(node)
        for nodes_used in top_node:
            temp = self.used_controllers_search(KG,nodes_used)
            if temp is not None:
                used_top_node.append(temp)

        for temp_node in used_top_node:
            if temp_node['type']=='N':
                true_top_company.append(temp_node)
            else:
                neighbor_nodes = KG.vs[KG.neighbors(temp_node)]
                investment_max = max([KG[temp_node, node] for node in neighbor_nodes])
                group_node = [next_node['name'] for next_node in neighbor_nodes if
                              KG.es[KG.get_eid(temp_node, next_node)]['weight'] == investment_max]
                true_top_company.append(group_node)
        return true_top_company
    def used_controllers_search(self,KG,nodes_used):# 用于确定  频繁控制人
        def traversal_node(node,nodes,KG):
            nodes_dfs=[]
            temp_top=[]
            temp_top.append(node)
            # KG_top = node
            if len(temp_top)<>0:
                KG_top = temp_top[0]
                neighbor_nodes = KG.vs[KG.neighbors(KG_top)]
                if len(neighbor_nodes)>0:
                    for neighbor_node in neighbor_nodes:
                        if neighbor_node not in nodes and (KG[ KG_top,neighbor_node]+KG[ neighbor_node,KG_top] )>= self.min_share_num:
                            nodes.append(neighbor_node)
                            nodes_dfs.append(neighbor_node)
                            temp_top.append(neighbor_node)
                temp_top.remove(KG_top)
            return nodes_dfs
        nodes = []
        nodes.append(nodes_used)
        nodes_dfs=traversal_node(nodes_used,nodes,KG)
        if len(nodes_dfs)>=self.max_controllers_num:
            return nodes_used
        else:
            return None
    def find_group_by_degree(self, KG):  # 根据出入度进行匹配，阈值由有监督学习提前设定
        group_list = []
        for temp_node in KG.vs:
            if temp_node.indegree() == self.group_indegree  and temp_node.outdegree() >=self.group_outdegree:
                group_list.append(temp_node['name'])
        group_list = list(set(group_list))
        return group_list

    # def find_group_by_character(self,company_information,organization_type_list):
    #     pass

    def combining_group_lists(self,group_lists): # 取并集
        group_list_A =[]
        # company_white_list = []
        # for group_list in group_lists:
        #     company_white_list.append (i for i in group_list)
        if len(group_lists)>0:
            for temp_list in group_lists:
                group_list_A = list(set(temp_list).union(set(group_list_A)))
                # list(set(listA).intersection(set(listB)))
        return group_list_A


