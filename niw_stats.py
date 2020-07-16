import win32com.client


import pandas as pd
import os
import matplotlib.pyplot as plt

df = pd.read_csv(r'Z:\Docs\DailyOperationalProcedures\Performance_Charts\CSV\csv_files\NIWEBSAPPPR01v_sar_stats.csv')
# captures the title from -  NIWEBSAPPPR01v Performance Chart Mon 01/07/20 - Fri 30/07/20 
title = df.columns[5]
# removes the sixth column [5] - NIWEBSAPPPR01v Performance Chart Mon 01/07/20 - Fri 30/07/20
df.drop(df.columns[[5]], axis=1, inplace=True)
# prints out the line graph plot
#new_df.plot(figsize=(12,8))
df.to_csv(r'C:\Users\MCARTHURP\Desktop\niw_stats\demo-file2.csv')
#df.to_csv('demo-file.csv')
# prints the sixth column [5] as a title
#pl.suptitle(column_list[5])
# print the new csv output
ax = df.plot(figsize=(12,8))
plt.suptitle(title)
#ax.figure.savefig(os.path.join(path,r'demo-file2.jpg'))
ax.figure.savefig(r'C:\Users\MCARTHURP\Desktop\niw_stats\demo-file2.jpg')



const=win32com.client.constants
olMailItem = 0x0
obj = win32com.client.Dispatch("Outlook.Application")
mail = obj.CreateItem(olMailItem)

signatureimage = r"C:\Users\MCARTHURP\Desktop\niw_stats\demo-file2.jpg"

#send_email(sender,recipient):
#mail = outlook.CreateItem(0)
mail.To = 'pmcarthur@**.com; paul.mcarthur@**.com; andrew.owens1@**.com'
mail.Subject = "TEST : NIW - Performance Stats : TEST"
attachment = mail.Attachments.Add(signatureimage)
attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", "MyId1")
mail.HTMLBody = "<html><body><img src=""cid:MyId1""></body></html>"


attachment1 = r"C:\Users\MCARTHURP\Desktop\niw_stats\demo-file2.csv"
#attachment2 = r"C:\Users\MCARTHURP\Desktop\niw_stats\demo-file2.jpg"
mail.Attachments.Add(Source=attachment1)
#mail.Attachments.Add(Source=attachment2)

#mail.SentOnBehalfOfName = sender
mail.GetInspector 
mail.Display()
#mail.Send()

#Change the Paths here, if ran from a different location
#signatureimage = r"C:\Users\MCARTHURP\Desktop\niw_stats\demo-file2.jpg"
