#!/usr/bin/env python
# coding: utf-8

import pandas as pd





cinfo = pd.read_csv("C:/Users/Hp/Desktop/assignment1/Customers_Information.csv")
cmash = pd.read_csv("C:/Users/Hp/Desktop/assignment1/Customer_Mashup.csv")
cpayinfo = pd.read_csv("C:/Users/Hp/Desktop/assignment1/Customers_payment_Information.csv")
provdata = pd.read_excel("C:/Users/Hp/Desktop/assignment1/provisioning-data.xlsx")





ctokeninfo = pd.read_csv("C:/Users/Hp/Desktop/assignment1/Customer_Token_Information.csv")
ctokeninfo = ctokeninfo.rename(columns= {"contractId":"ContractId"})
ctokeninfo = ctokeninfo.set_index("ContractId")

cchangedata = pd.read_excel("C:/Users/Hp/Desktop/assignment1/customer-changing-data (1).xlsx")


mashinfo = pd.merge(cmash, cinfo, on= ["AccountNumber", "ContractId", "CustomerId", "ContractStatus"])
cstatus= mashinfo.loc[:, ["ContractId", "AccountNumber", "CustomerId", "ContractStatus"]]
provdata = provdata.rename(columns={"Loan_Id": "ContractId"})




sts= pd.merge(cstatus, provdata, on=["ContractId"]).drop(columns=["ContractStatus"
                                                                  ]).rename(columns={"customerStatus": "Status"})



problem1solution = sts
print(problem1solution)










