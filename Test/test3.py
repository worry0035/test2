from pyecharts import  options as opts
from pyecharts.charts import  Graph
nodes = [
    {'name':'第一章','symbolSize':10},
    {'name':'第二章','symbolSize':10},
    {'name':'第三章','symbolSize':10},
    {'name':'第四章','symbolSize':10},
    {'name':'第五章','symbolSize':10},
    {'name':'第7 章','symbolSize':10},
]
links = []
for i in nodes:
    for j in nodes:
        links.append({'source':i.get('name'),'target':j.get('name')})
c = (
    Graph().
    add(
        '',
        nodes,
        links,
        repulsion=5000
    )
    .set_global_opts(title_opts=opts.TitleOpts(title='关系图'))
)
c.render()