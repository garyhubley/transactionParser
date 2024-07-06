Attribute VB_Name = "Module1"
Sub NamedRanges()
    ActiveWorkbook.Names.Add Name:="Pages", RefersTo:="=Sheet1!$A$2:$A$9"
    ActiveWorkbook.Names.Add Name:="HousePg", RefersTo:="=Sheet1!$C$2:$C$5"
    ActiveWorkbook.Names.Add Name:="DailyPg", RefersTo:="=Sheet1!$C$6:$C$9"
    ActiveWorkbook.Names.Add Name:="HealthPg", RefersTo:="=Sheet1!$C$10:$C$10"
    ActiveWorkbook.Names.Add Name:="DependentsPg", RefersTo:="=Sheet1!$C$11:$C$12"
    ActiveWorkbook.Names.Add Name:="EntertainmentPg", RefersTo:="=Sheet1!$C$13:$C$15"
    ActiveWorkbook.Names.Add Name:="TransportPg", RefersTo:="=Sheet1!$C$16"
    ActiveWorkbook.Names.Add Name:="AccountsPg", RefersTo:="=Sheet1!$C$17:$C$19"
    ActiveWorkbook.Names.Add Name:="IncomePg", RefersTo:="=Sheet1!$C$20:$C$21"
    ActiveWorkbook.Names.Add Name:="Utilities", RefersTo:="=Sheet1!$A$24:$A$28"
    ActiveWorkbook.Names.Add Name:="Professional", RefersTo:="=Sheet1!$C$24:$C$27"
    ActiveWorkbook.Names.Add Name:="House", RefersTo:="=Sheet1!$A$33:$A$36"
    ActiveWorkbook.Names.Add Name:="Subscriptions", RefersTo:="=Sheet1!$C$33:$C$41"
    ActiveWorkbook.Names.Add Name:="Food", RefersTo:="=Sheet1!$E$24:$E$27"
    ActiveWorkbook.Names.Add Name:="Clothing", RefersTo:="=Sheet1!$G$24:$G$28"
    ActiveWorkbook.Names.Add Name:="Grooming", RefersTo:="=Sheet1!$G$33:$G$36"
    ActiveWorkbook.Names.Add Name:="Supplies", RefersTo:="=Sheet1!$I$24:$I$30"
    ActiveWorkbook.Names.Add Name:="Health", RefersTo:="=Sheet1!$I$33:$I$41"
    ActiveWorkbook.Names.Add Name:="Barney", RefersTo:="=Sheet1!$A$44:$A$51"
    ActiveWorkbook.Names.Add Name:="Children", RefersTo:="=Sheet1!$C$44:$C$52"
    ActiveWorkbook.Names.Add Name:="Sports", RefersTo:="=Sheet1!$G$44:$G$47"
    ActiveWorkbook.Names.Add Name:="Entertainment", RefersTo:="=Sheet1!$I$44:$I$50"
    ActiveWorkbook.Names.Add Name:="Vacations", RefersTo:="=Sheet1!$G$2:$G$12"
    ActiveWorkbook.Names.Add Name:="Transportation", RefersTo:="=Sheet1!$A$58:$A$69"
    ActiveWorkbook.Names.Add Name:="Debt", RefersTo:="=Sheet1!$C$58:$C$59"
    ActiveWorkbook.Names.Add Name:="Savings", RefersTo:="=Sheet1!$I$2:$I$9"
    ActiveWorkbook.Names.Add Name:="Accounts", RefersTo:="=Sheet1!$E$2:$E$6"
    ActiveWorkbook.Names.Add Name:="ChristinaIncome", RefersTo:="=Sheet1!$E$44:$E$47"
    ActiveWorkbook.Names.Add Name:="GaryIncome", RefersTo:="=Sheet1!$E$33:$E$35"
End Sub

Sub AddValidation()
    Dim Cnt As Long
    Cnt = WorksheetFunction.CountA(Range("A:A"))
    Set Rng = Range(Cells(2, 6), Cells(Cnt, 6))
    With Rng.Validation
        .Delete
        .Add Type:=xlValidateList, AlertStyle:=xlValidAlertStop, Formula1:="=Pages"
    End With
    
    For i = 2 To Cnt
        colF = "f" & i
        Range(colF).Value = "HousePg"
        colG = "g" & i
        colH = "h" & i
        With Range(colG).Validation
            .Delete
            .Add Type:=xlValidateList, AlertStyle:=xlValidAlertStop, _
                    Operator:=xlBetween, Formula1:="=INDIRECT(" & Range(colF).Address(False, False) & ")"
        End With
        Range(colG).Value = "Utilities"
        With Range(colH).Validation
            .Delete
            .Add Type:=xlValidateList, AlertStyle:=xlValidAlertStop, _
                    Operator:=xlBetween, Formula1:="=INDIRECT(" & Range(colG).Address(False, False) & ")"
        End With
        Range(colF).Value = ""
        Range(colG).Value = ""
    Next i

End Sub

