Sub CopyAndProcessSheet_Final()

    Dim wb As Workbook
    Dim wsSrc As Worksheet
    Dim wsNew As Worksheet
    
    Dim lastRow As Long
    Dim lastCol As Long
    Dim firstNumRow As Long
    Dim firstInputRow As Long
    Dim startRow As Long
    Dim endRow As Long
    
    Dim i As Long
    Dim r As Long
    Dim cellVal As Variant
    
    Dim currentCategory As Long
    Dim numericCount As Long
    Dim stepMs As Double
    Dim elapsedMs As Double
    
    Dim firstVal As Double
    Dim secondVal As Double
    Dim foundFirst As Boolean
    Dim foundSecond As Boolean
    
    Set wb = ThisWorkbook
    Set wsSrc = wb.Worksheets(1)
    
    wsSrc.Copy After:=wb.Worksheets(1)
    Set wsNew = wb.Worksheets(2)
    
    ' A列の最初の数値行より上を削除
    lastRow = wsNew.Cells(wsNew.Rows.Count, 1).End(xlUp).Row
    firstNumRow = 0
    
    For i = 1 To lastRow
        cellVal = wsNew.Cells(i, 1).Value
        If Trim(cellVal & "") <> "" Then
            If IsNumeric(cellVal) Then
                firstNumRow = i
                Exit For
            End If
        End If
    Next i
    
    If firstNumRow = 0 Then
        MsgBox "A列に数値データが見つかりませんでした。", vbExclamation
        Exit Sub
    End If
    
    If firstNumRow > 1 Then
        wsNew.Rows("1:" & firstNumRow - 1).Delete
    End If
    
    ' A,D,G列のみ残す
    lastCol = wsNew.Cells(1, wsNew.Columns.Count).End(xlToLeft).Column
    For i = lastCol To 1 Step -1
        If i <> 1 And i <> 4 And i <> 7 Then
            wsNew.Columns(i).Delete
        End If
    Next i
    
    ' 元データの刻み幅取得
    stepMs = 2
    foundFirst = False
    foundSecond = False
    
    lastRow = wsNew.Cells(wsNew.Rows.Count, 1).End(xlUp).Row
    For i = 1 To lastRow
        cellVal = wsNew.Cells(i, 1).Value
        If Trim(cellVal & "") <> "" And IsNumeric(cellVal) Then
            If Not foundFirst Then
                firstVal = CDbl(cellVal)
                foundFirst = True
            Else
                secondVal = CDbl(cellVal)
                foundSecond = True
                Exit For
            End If
        End If
    Next i
    
    If foundFirst And foundSecond Then
        stepMs = secondVal - firstVal
        If stepMs <= 0 Then stepMs = 2
    End If
    
    ' 列構成を A,カテゴリA,カテゴリB,D,G にする
    wsNew.Columns(2).Insert Shift:=xlToRight
    wsNew.Columns(2).Insert Shift:=xlToRight
    
    ' ヘッダ行追加
    wsNew.Rows(1).Insert Shift:=xlDown
    wsNew.Cells(1, 1).Value = "経過時間(ms)"
    wsNew.Cells(1, 2).Value = "カテゴリ(A)"
    wsNew.Cells(1, 3).Value = "カテゴリ(B)"
    wsNew.Cells(1, 4).Value = "左目瞳孔面積"
    wsNew.Cells(1, 5).Value = "右目瞳孔面積"
    
    lastRow = wsNew.Cells(wsNew.Rows.Count, 1).End(xlUp).Row
    wsNew.Range(wsNew.Cells(2, 2), wsNew.Cells(lastRow, 3)).Value = 0
    
    ' 最初のINPUTを探す
    firstInputRow = 0
    For i = 2 To lastRow
        cellVal = wsNew.Cells(i, 1).Value
        If VarType(cellVal) = vbString Then
            If InStr(1, cellVal, "INPUT", vbTextCompare) > 0 Then
                firstInputRow = i
                Exit For
            End If
        End If
    Next i
    
    If firstInputRow = 0 Then
        MsgBox "A列にINPUTが見つかりませんでした。", vbExclamation
        Exit Sub
    End If
    
    ' 最初のINPUTの前にある数値データ250個前を開始位置にする
    numericCount = 0
    startRow = 2
    
    For r = firstInputRow - 1 To 2 Step -1
        cellVal = wsNew.Cells(r, 1).Value
        If Trim(cellVal & "") <> "" And IsNumeric(cellVal) Then
            numericCount = numericCount + 1
            If numericCount = 250 Then
                startRow = r
                Exit For
            End If
        End If
    Next r
    
    ' 5000個の数値データ分を対象にする
    endRow = lastRow
    numericCount = 0
    
    For r = startRow To lastRow
        cellVal = wsNew.Cells(r, 1).Value
        If Trim(cellVal & "") <> "" And IsNumeric(cellVal) Then
            numericCount = numericCount + 1
            If numericCount = 5000 Then
                endRow = r
                Exit For
            End If
        End If
    Next r
    
    ' カテゴリ付与
    currentCategory = 1
    For i = startRow To endRow
        cellVal = wsNew.Cells(i, 1).Value
        
        If VarType(cellVal) = vbString Then
            If InStr(1, cellVal, "INPUT", vbTextCompare) > 0 Then
                If currentCategory = 1 Then
                    currentCategory = 2
                Else
                    currentCategory = 1
                End If
            End If
        End If
        
        If currentCategory = 1 Then
            wsNew.Cells(i, 2).Value = 1
            wsNew.Cells(i, 3).Value = 0
        Else
            wsNew.Cells(i, 2).Value = 0
            wsNew.Cells(i, 3).Value = 1
        End If
    Next i
    
    ' A列の文字列行を削除
    lastRow = wsNew.Cells(wsNew.Rows.Count, 1).End(xlUp).Row
    For i = lastRow To 2 Step -1
        cellVal = wsNew.Cells(i, 1).Value
        If Trim(cellVal & "") <> "" Then
            If Not IsNumeric(cellVal) Then
                wsNew.Rows(i).Delete
            End If
        End If
    Next i
    
    ' 経過時間を完全に振り直す
    lastRow = wsNew.Cells(wsNew.Rows.Count, 4).End(xlUp).Row
    elapsedMs = 0
    
    For i = 2 To lastRow
        elapsedMs = elapsedMs + stepMs
        wsNew.Cells(i, 1).Value = elapsedMs
    Next i
    
    wsNew.Columns(1).NumberFormat = "0"
    
    MsgBox "処理が完了しました。", vbInformation

End Sub
