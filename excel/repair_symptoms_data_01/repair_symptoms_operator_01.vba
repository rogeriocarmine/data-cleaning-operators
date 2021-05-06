Public Function IsInArray(stringToBeFound As String, arr As Variant) As Boolean
    Dim i
    For i = LBound(arr) To UBound(arr)
        If arr(i) = stringToBeFound Then
            IsInArray = True
            Exit Function
        End If
    Next i
    IsInArray = False

End Function


Sub repairsymptoms()
'
' repairsymptoms Macro
'
Dim Result As Boolean
Dim Yes As Variant
Dim No As Variant

Yes = Array("SIM", "YES", "Y", "X", "SI","OK")
No = Array("NAO", "NO", "N")

' Change the Sheet and Range according to the case.

Set RangeToFix = Sheets("outbreak_dataset").Range("G2:G201")

For Each Cell In RangeToFix
        If IsInArray(UCase(Cell.Value), Yes) Then
            Cell.Value = 1
        Else
            If IsInArray(UCase(Cell.Value), No) Then
               Cell.Value = 0
            End If
        End If
Next Cell
   
End Sub