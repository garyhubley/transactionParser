Attribute VB_Name = "Module1"
Sub NamedRanges()
    ActiveWorkbook.Names.Add Name:="Tables", RefersTo:="=Sheet1!$C$1:$C$20"
	ActiveWorkbook.Names.Add Name:="tblUtilities", RefersTo:="=Sheet1!$A$2:$A$6"
	ActiveWorkbook.Names.Add Name:="tblProfessional", RefersTo:="=Sheet1!$A$9:$A$12"
	ActiveWorkbook.Names.Add Name:="tblHouse", RefersTo:="=Sheet1!$A$15:$A$18"
	ActiveWorkbook.Names.Add Name:="tblSubscriptions", RefersTo:="=Sheet1!$A$21:$A$27"
	ActiveWorkbook.Names.Add Name:="tblFood", RefersTo:="=Sheet1!$A$30:$A$33"
	ActiveWorkbook.Names.Add Name:="tblClothing", RefersTo:="=Sheet1!$A$36:$A$40"
	ActiveWorkbook.Names.Add Name:="tblGrooming", RefersTo:="=Sheet1!$A$43:$A$46"
	ActiveWorkbook.Names.Add Name:="tblSupplies", RefersTo:="=Sheet1!$A$49:$A$56"
	ActiveWorkbook.Names.Add Name:="tblHealth", RefersTo:="=Sheet1!$A$59:$A$69"
	ActiveWorkbook.Names.Add Name:="tblBarney", RefersTo:="=Sheet1!$A$72:$A$79"
	ActiveWorkbook.Names.Add Name:="tblChildren", RefersTo:="=Sheet1!$A$82:$A$89"
	ActiveWorkbook.Names.Add Name:="tblSports", RefersTo:="=Sheet1!$A$92:$A$95"
	ActiveWorkbook.Names.Add Name:="tblEntertainment", RefersTo:="=Sheet1!$A$98:$A$104"
	ActiveWorkbook.Names.Add Name:="tblVacation", RefersTo:="=Sheet1!$A$107:$A$117"
	ActiveWorkbook.Names.Add Name:="tblTransportation", RefersTo:="=Sheet1!$A$120:$A$131"
	ActiveWorkbook.Names.Add Name:="tblDebt", RefersTo:="=Sheet1!$A$134:$A$136"
	ActiveWorkbook.Names.Add Name:="tblSavings", RefersTo:="=Sheet1!$A$139:$A$145"
	ActiveWorkbook.Names.Add Name:="tblAccounts", RefersTo:="=Sheet1!$A$148:$A$151"
	ActiveWorkbook.Names.Add Name:="tblChristinaIncome", RefersTo:="=Sheet1!$A$154:$A$156"
	ActiveWorkbook.Names.Add Name:="tblGaryIncome", RefersTo:="=Sheet1!$A$159:$A$161"
End Sub

Sub AddValidation()
    Dim Cnt As Long
    Cnt = WorksheetFunction.CountA(Range("A:A"))
    Set Rng = Range(Cells(2, 6), Cells(Cnt, 6))
    With Rng.Validation
        .Delete
        .Add Type:=xlValidateList, AlertStyle:=xlValidAlertStop, Formula1:="=Tables"
    End With
    
    For i = 2 To Cnt
        colF = "f" & i
        Range(colF).Value = "tblUtilities"
        colG = "g" & i
        With Range(colG).Validation
            .Delete
            .Add Type:=xlValidateList, AlertStyle:=xlValidAlertStop, _
                    Operator:=xlBetween, Formula1:="=INDIRECT(" & Range(colF).Address(False, False) & ")"
        End With
        Range(colF).Value = ""
    Next i

End Sub

