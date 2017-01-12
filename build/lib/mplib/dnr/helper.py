# coding: utf-8
# __author__: u"John"
import pandas as pd
import csv


# 导出Excel文件
def export_to_excel(data_list, file_name, column_head):
    df = pd.DataFrame(data_list, columns=column_head)
    writer = pd.ExcelWriter(file_name)
    df.to_excel(writer, sheet_name=u"NDR_API_processed", encoding=u"utf-8", engine=u"xlsxwriter")
    writer.save()
    writer.close()
    return


# 导出txt文件
def export_to_txt(data_list, file_name, column_head):
    if len(column_head) > 0:
        att_head = True
    else:
        att_head = False
        column_head = None
    df = pd.DataFrame(data_list, columns=column_head)
    df.to_csv(file_name, encoding=u'utf-8', index=None, sep='\t', mode='w', quoting=csv.QUOTE_NONE,
              header=att_head)
    return


if __name__ == u"__main__":
    # export_to_excel([u"a", u"b", u"c", u"d"], u"啊", [u"ha"])
    export_to_txt([u"a", u"b", u"c", u"d"], u"啊.txt", column_head=None)
