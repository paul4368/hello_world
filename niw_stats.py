# NIW Sar Stats  -  this python code will import and process the sar cvs files that are emailed into the team mailbox each week #

import win32com.client


import pandas as pd
import os
import matplotlib.pyplot as plt

# NIWEBSAPPPR01v
df = pd.read_csv(
    r'Z:\Docs\DailyOperationalProcedures\Performance_Charts\CSV\csv_files\NIWEBSAPPPR01v_sar_stats.csv')
# captures the title from column 5 -  NIWEBSAPPPR01v Performance Chart Mon **/**/20 - Fri **/**/20
title = df.columns[5]
# removes the sixth column [5] - NIWEBSAPPPR01v Performance Chart Mon **/**/20 - Fri **/**/20 - tidies up the cvs file
df.drop(df.columns[[5]], axis=1, inplace=True)
# saves the new csv file
df.to_csv(r'Z:\Docs\DailyOperationalProcedures\Performance_Charts\CSV\NIWEBSAPPPR01v.csv')
# saves the new plot output to a png file
ax = df.plot(figsize=(12, 8))
plt.xlabel('Time in 10min intervals i.e 120 = 24Hr')
#plt.ylabel('% percentage')
plt.suptitle(title)
ax.figure.savefig(r'Z:\Docs\DailyOperationalProcedures\Performance_Charts\CSV\png_files\NIWEBSAPPPR01v.png')

# NIWEBSDBPR01v
df = pd.read_csv(
    r'Z:\Docs\DailyOperationalProcedures\Performance_Charts\CSV\csv_files\NIWEBSDBPR01v_sar_stats.csv')
# captures the title from -  NIWEBSAPPPR01v Performance Chart Mon 01/07/20 - Fri 30/07/20
title = df.columns[5]
# removes the sixth column [5] - NIWEBSAPPPR01v Performance Chart Mon 01/07/20 - Fri 30/07/20
df.drop(df.columns[[5]], axis=1, inplace=True)
# saves the new csv file
df.to_csv(r'Z:\Docs\DailyOperationalProcedures\Performance_Charts\CSV\NIWEBSDBPR01v.csv')
# saves the new piot output to a png file
ax = df.plot(figsize=(12, 8))
plt.xlabel('Time in 10min intervals i.e 120 = 24Hr')
#plt.ylabel('% percentage')
plt.suptitle(title)
ax.figure.savefig(r'Z:\Docs\DailyOperationalProcedures\Performance_Charts\CSV\png_files\NIWEBSDBPR01v.png')

# the outlook bit
const = win32com.client.constants
olMailItem = 0x0
obj = win32com.client.Dispatch("Outlook.Application")
mail = obj.CreateItem(olMailItem)

# Change the Paths here, if ran from a different location
signatureimage = r"Z:\Docs\DailyOperationalProcedures\Performance_Charts\CSV\png_files\NIWEBSDBPR01v.png"
signatureimage2 = r"Z:\Docs\DailyOperationalProcedures\Performance_Charts\CSV\png_files\NIWEBSAPPPR01v.png"

# where the email is going
mail.To = '*****@***.com; *****@***.com; *****@***.com; ******@***.com'
mail.Subject = "NIW - Performance Stats : NIWEBSDBPR01v & NIWEBSAPPPR01v"

#adding the attachments and imbedded png files
attachment = mail.Attachments.Add(signatureimage)
attachment2 = mail.Attachments.Add(signatureimage2)

attachment.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", "MyId1")


attachment2.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", "MyId2")
mail.HTMLBody = "<html><body><img src=""cid:MyId1""><br><img src=""cid:MyId2""></body></html>"

attachment1 = r"Z:\Docs\DailyOperationalProcedures\Performance_Charts\CSV\NIWEBSDBPR01v.csv"
attachment2 = r"Z:\Docs\DailyOperationalProcedures\Performance_Charts\CSV\NIWEBSAPPPR01v.csv"
mail.Attachments.Add(Source=attachment1)
mail.Attachments.Add(Source=attachment2)


mail.GetInspector
mail.Display()
# mail.Send() #unhash to send email directly from script#
# print(df) #this will print out the csv contents if unhashed#
