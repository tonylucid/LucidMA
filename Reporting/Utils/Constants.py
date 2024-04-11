### TRANSACTION MAP ###
transaction_map = {
    "ASSIGN (BEG)": "Beginning Cap Acct Bal",
    "BAL FWD": "Beginning Cap Acct Bal",
    "CE AD COST": "Expense",
    "CE ADMIN": "Expense",
    "CE AUDIT": "Expense",
    "CE CUST FE": "Expense",
    "CE FCE": "Expense",
    "CE HED FEE": "Expense",
    "CE IF": "Mgmt Fee Waiver",
    "CE IIEA": "Income",
    "CE IIEM": "Income",
    "CE IIF": "Income",
    "CE IIM": "Income",
    "CE IIMM": "Income",
    "CE IIR": "Income",
    "CE MF": "Mgmt Fee",
    "CE MFW": "Mgmt Fee Waiver",
    "CE MREAL": "Mark to Market",
    "CE MUNREAL": "Mark to Market",
    "CE ORG EXP": "Expense",
    "CE OTH FEE": "Expense",
    "CE RADJEXP": "Expense",
    "CE RADJINC": "Income",
    "CONT": "Contribution",
    "Total": "Ending Cap Acct Bal",
    "WITH (BEG)": "Withdrawal - BOP",
    "WITH (END)": "Withdrawal - EOP",
}

# Define the columns needed for the Bronze returns table
needed_columns = [
    "SK",
    "VehicleCode",
    "VehicleDescription",
    "PoolCode",
    "PoolDescription",
    "Period",
    "PeriodDescription",
    "InvestorCode",
    "InvestorDescription",
    "Head1",
    "Amt1",
]

master_data_return_column_order = [
    "Start Date", "End Date", "Starting Cap Accounts", "End Cap Accounts",
    "Admin NAV Strike Date", "Subscriptions", "Withdrawals", "Gross Return",
    "Net Return (Act/360)", "Net Return (Act/365)",
    "Principal Outstanding", "Interest Payment Date", "Interest Paid", "Benchmark",
    "Benchmark return", "Outperform", "Target Outperform", "1m SOFR",
    "1m T-Bills", "US Gov't & AAA (%)", "AA to A (%)",
    "BBB (%)", "HY (%)", "A1/P1 CP", "T-Bills /Govt MMF", "Total OC Rate", "US Gov't & AAA",
    "AA to A", "BBB", "HY", "Benchmark File", "Comments"
]

cash_balance_column_order = [
    "Fund", "Series", "Account", "Cash Balance", "Sweep Balance", "Projected Total Balance"
]

investor_mapping = {'1000076533': 'The Nemours Foundation', '1000076536': 'Alfred I. duPont Charitable Trust', '1000076535': 'The Nemours Foundation - Intermediate Account', '1000076534': 'The Nemours Foundation Pension Plan', '1000075632': 'Prime Notes Series MIG-1', '1000075037': 'Prime Notes Series M1-1', '1000075042': "Children's Health System of Texas", '1000074096': 'The New York and Presbyterian Hospital', '1000073585': 'Prime Notes LLC Series Q1-1', '1000073123': 'Prime Notes LLC Series M-1', '1000072321': 'Hudson East River Systems, LLC', '1000071470': 'IRR K LLC', '1000070673': 'The Kresge Foundation', '1000068425': 'Lucid Management and Capital Partners LP', '1000068282': 'University of Virginia Investment Mgmt Company', '1000079112': 'In Touch Media, Inc.', '1000079039': 'The Southern Baptist Theological Seminary', '1000078809': 'Prime Notes Series Q364-1', '1000078306': 'In Touch Ministries, Inc.', '1000078307': 'In Touch Foundation, Inc.', '1000078109': 'Word of God Fellowship, Inc.', '1000078103': 'International Mission Board of Southern Baptist Convention', '1000077312': 'Prime Notes Series QX-1', '1000076859': 'Amica Retiree Medical Trust', '1000081062': 'Dr. Otis S. Hawkins', '1000081109': 'GuideStone Trust Services', '1000080932': 'Prime Notes Series 2YIG-1', '1000080888': 'New York City Ballet, Inc.', '1000080775': 'Executive Committee of the Baptist Convention of the State of Georgia (d/b/a Georgia Baptist Mission Board)', '1000080594': 'Prime Notes Series MIG-2', '1000080593': 'Prime Notes Series A1-1', '1000080538': 'Word of God Fellowship, Inc. Cash Reserves', '1000080312': 'MFIF Holdings Blue, L.P.', '1000080313': 'Makena Capital Holdings B, LP', '163976002': 'GuideStone Financial Resources of the Southern Baptist Convention - Operating Reserves', '166129001': 'The Nemours Foundation - Intermediate Account (Sleeve 1)', '163976001': 'Guidestone Financial Resources of the Southern Baptist Convention - Operating Reserves', '27132001': 'Georgia Tech Foundation, Inc', '162038001': 'Prime Notes Series MIG-3', '160529001': 'Guidestone Financial Resources of the Southern Baptist Convention (FBO Fixed Benefit Fund)', '158823001': 'American Heart Association, Inc.', '1000081422': 'Prime Notes Series Q1-2', '1000081292': 'Prime Notes Series M-2', '1000076858': 'Amica Pension Fund', '1000081293': 'Prime Notes Series M-3', '159721001': 'Christian Financial Resources, Inc.', '27132': 'Georgia Tech Foundation, Inc', '155720001': 'The Nemours Foundation - Intermediate Account (Sleeve 1)', '1000066724': 'The Kresge Foundation', '1000075471': 'USG Assets Series M-5', '1000074147': 'USG ASSETS LLC Series M-4', '1000062947': 'Lucid Management and Capital Partners LLC', '1000142910': 'USG ASSETS LLC Series M-7', '1000078839': 'USG Assets Series M-6', '1000079679': 'USG ASSETS LLC Series M-7', '165929001': 'USG Assets Series M-8', '155696001': "Children's Health System of Texas", '28966001': "Children's Medical Center Foundation", '167488001': 'USG Assets Series M-9'}
period_mapping = {'2021-129': 'From 1/29/2021 To 1/31/2021', '2021-115': 'From 1/15/2021 To 1/28/2021', '2021-105': 'From 1/5/2021 To 1/14/2021', '2021-001': 'From 1/1/2021 To 1/4/2021', '22-0121': 'From 1/21/2022 To 1/31/2022', '22-0114': 'From 1/14/2022 To 1/20/2022', '22-0101': 'From 1/1/2022 To 1/13/2022', '23-0113': 'From 1/13/2023 To 1/19/2023', '23-0120': 'From 1/20/2023 To 1/31/2023', '23-0101': 'From 1/1/2023 To 1/12/2023', '24-0101': 'From 1/1/2024 To 1/11/2024', '24-0119': 'From 1/19/2024 To 1/31/2024', '24-0112': 'From 1/12/2024 To 1/18/2024', '2021-226': 'From 2/26/2021 To 2/28/2021', '2021-219': 'From 2/19/2021 To 2/25/2021', '2021-212': 'From 2/12/2021 To 2/18/2021', '2021-002': 'From 2/1/2021 To 2/11/2021', '22-0211': 'From 2/11/2022 To 2/28/2022', '22-0201': 'From 2/1/2022 To 2/10/2022', '23-0217': 'From 2/17/2023 To 2/28/2023', '23-0210': 'From 2/10/2023 To 2/16/2023', '23-0201': 'From 2/1/2023 To 2/9/2023', '24-0223': 'From 2/23/2024 To 2/29/2024', '24-0216': 'From 2/16/2024 To 2/22/2024', '24-0201': 'From 2/1/2024 To 2/15/2024', '2021-326': 'From 3/26/2021 To 3/31/2021', '2021-323': 'From 3/23/2021 To 3/25/2021', '2021-312': 'From 3/12/2021 To 3/22/2021', '2021-003': 'From 3/1/2021 To 3/11/2021', '22-0311': 'From 3/11/2022 To 3/31/2022', '22-0301': 'From 3/1/2022 To 3/10/2022', '23-0316': 'From 3/16/2023 To 3/21/2023', '23-0322': 'From 3/22/2023 To 3/31/2023', '23-0310': 'From 3/10/2023 To 3/15/2023', '23-0301': 'From 3/1/2023 To 3/9/2023', '2021-416': 'From 4/16/2021 To 4/30/2021', '2021-409': 'From 4/9/2021 To 4/15/2021', '2021-004': 'From 4/1/2021 To 4/8/2021', '22-0429': 'From 4/29/2022 To 4/30/2022', '22-0415': 'From 4/15/2022 To 4/28/2022', '22-0401': 'From 4/1/2022 To 4/14/2022', '23-0414': 'From 4/14/2023 To 4/30/2023', '23-0405': 'From 4/5/2023 To 4/13/2023', '23-0401': 'From 4/1/2023 To 4/4/2023', '2021-514': 'From 5/14/2021 To 5/31/2021', '2021-005': 'From 5/1/2021 To 5/13/2021', '22-0513': 'From 5/13/2022 To 5/31/2022', '22-0501': 'From 5/1/2022 To 5/12/2022', '23-0512': 'From 5/12/2023 To 5/31/2023', '23-0505': 'From 5/5/2023 To 5/11/2023', '23-0501': 'From 5/1/2023 To 5/4/2023', '2021-611': 'From 6/11/2021 To 6/17/2021', '2021-006': 'From 6/1/2021 To 6/10/2021', '2021-618': 'From 6/18/2021 To 6/30/2021', '22-0610': 'From 6/10/2022 To 6/30/2022', '22-0601': 'From 6/1/2022 To 6/9/2022', '23-0623': 'From 6/23/2023 To 6/30/2023', '23-0616': 'From 6/16/2023 To 6/22/2023', '23-0610': 'From 6/10/2023 To 6/15/2023', '23-0601': 'From 6/1/2023 To 6/9/2023', '2021-723': 'From 7/23/2021 To 7/31/2021', '2021-716': 'From 7/16/2021 To 7/22/2021', '2021-007': 'From 7/1/2021 To 7/15/2021', '22-0715': 'From 7/15/2022 To 7/31/2022', '22-0701': 'From 7/1/2022 To 7/14/2022', '21-0416': 'From 4/16/2021 To 4/30/2021', '21-0105': 'From 1/5/2021 To 1/14/2021', '23-0721': 'From 7/21/2023 To 7/31/2023', '23-0714': 'From 7/14/2023 To 7/20/2023', '23-0701': 'From 7/1/2023 To 7/13/2023', '21-0514': 'From 5/14/2021 To 5/31/2021', '21-0501': 'From 5/1/2021 To 5/13/2021', '21-0201': 'From 2/1/2021 To 2/11/2021', '21-0129': 'From 1/29/2021 To 1/31/2021', '21-0115': 'From 1/15/2021 To 1/28/2021', '21-0101': 'From 1/1/2021 To 1/4/2021', '21-0323': 'From 3/23/2021 To 3/25/2021', '21-0813': 'From 8/13/2021 To 8/26/2021', '21-0801': 'From 8/1/2021 To 8/12/2021', '21-0716': 'From 7/16/2021 To 7/22/2021', '21-0701': 'From 7/1/2021 To 7/15/2021', '21-0618': 'From 6/18/2021 To 6/30/2021', '21-0611': 'From 6/11/2021 To 6/17/2021', '21-0601': 'From 6/1/2021 To 6/10/2021', '21-0827': 'From 8/27/2021 To 8/31/2021', '21-0409': 'From 4/9/2021 To 4/15/2021', '21-0401': 'From 4/1/2021 To 4/8/2021', '21-0326': 'From 3/26/2021 To 3/31/2021', '21-0723': 'From 7/23/2021 To 7/31/2021', '21-0312': 'From 3/12/2021 To 3/22/2021', '21-0301': 'From 3/1/2021 To 3/11/2021', '21-0226': 'From 2/26/2021 To 2/28/2021', '21-0219': 'From 2/19/2021 To 2/25/2021', '21-0212': 'From 2/12/2021 To 2/18/2021', '22-0826': 'From 8/26/2022 To 8/31/2022', '22-0812': 'From 8/12/2022 To 8/25/2022', '22-0801': 'From 8/1/2022 To 8/11/2022', '23-0818': 'From 8/18/2023 To 8/31/2023', '23-0801': 'From 8/1/2023 To 8/17/2023', '21-0930': 'From 9/30/2021 To 9/30/2021', '21-0910': 'From 9/10/2021 To 9/29/2021', '21-0901': 'From 9/1/2021 To 9/9/2021', '22-0909': 'From 9/9/2022 To 9/30/2022', '22-0901': 'From 9/1/2022 To 9/8/2022', '23-0922': 'From 9/22/2023 To 9/30/2023', '23-0916': 'From 9/16/2023 To 9/21/2023', '23-0915': 'From 9/15/2023 To 9/15/2023', '23-0901': 'From 9/1/2023 To 9/14/2023', '21-1027': 'From 10/27/2021 To 10/31/2021', '21-1015': 'From 10/15/2021 To 10/26/2021', '21-1001': 'From 10/1/2021 To 10/14/2021', '22-1001': 'From 10/1/2022 To 10/13/2022', '22-1014': 'From 10/14/2022 To 10/31/2022', '21-1111': 'From 11/11/2021 To 11/30/2021', '21-1101': 'From 11/1/2021 To 11/10/2021', '22-1118': 'From 11/18/2022 To 11/30/2022', '22-1111': 'From 11/11/2022 To 11/17/2022', '22-1101': 'From 11/1/2022 To 11/10/2022', '23-1117': 'From 11/17/2023 To 11/30/2023', '23-1103': 'From 11/3/2023 To 11/16/2023', '23-1101': 'From 11/1/2023 To 11/2/2023', '23-1027': 'From 10/27/2023 To 10/31/2023', '23-1020': 'From 10/20/2023 To 10/26/2023', '23-1013': 'From 10/13/2023 To 10/19/2023', '23-1006': 'From 10/6/2023 To 10/12/2023', '23-1001': 'From 10/1/2023 To 10/5/2023', '21-1223': 'From 12/23/2021 To 12/31/2021', '21-1210': 'From 12/10/2021 To 12/22/2021', '21-1201': 'From 12/1/2021 To 12/9/2021', '22-1209': 'From 12/9/2022 To 12/31/2022', '22-1201': 'From 12/1/2022 To 12/8/2022', '23-1222': 'From 12/22/2023 To 12/31/2023', '23-1215': 'From 12/15/2023 To 12/21/2023', '23-1201': 'From 12/1/2023 To 12/14/2023', '22-0107': 'From 1/7/2022 To 1/13/2022', '22-0525': 'From 5/25/2022 To 5/31/2022', '22-0511': 'From 5/11/2022 To 5/12/2022', '23-0615': 'From 6/16/2023 To 6/30/2023', '21-1105': 'From 11/5/2021 To 11/10/2021'}
pool_mapping = {'GEN-LUCIDII': 'Lucid Prime Fund LLC', 'GEN-LUCIDII_MIG': 'Lucid Prime Fund LLC_MIG', 'GEN-LUCIDII_M1': 'Lucid Prime Fund LLC_M1', 'GEN-LUCIDII_C1': 'Lucid Prime Fund LLC_C1', 'GEN-LUCIDII_Q1': 'Lucid Prime Fund LLC_Q1', 'GEN-LUCIDII_QX': 'Lucid Prime Fund LLC_QX', 'GEN-LUCIDIIQ364': 'Lucid Prime Fund LLC_Q364', 'GEN-LUCIDII_S1': 'Lucid Prime Fund LLC_S1', 'GEN-LUCIDII_2YI': 'Lucid Prime Fund LLC_2YIG', 'GEN-LUCIDII_A1': 'Lucid Prime Fund LLC_A1', 'GEN-LUCID': 'Lucid Cash Fund USG LLC'}
vehicle_mapping = {'LUCID': 'Lucid Cash Fund USG LLC', 'LUCIDII': 'Lucid Prime Fund LLC'}
