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


Sub repairgenders()
'
' repairgenders Macro
'
Dim Result As Boolean
Dim Yes As Variant
Dim No As Variant

' Change the Sheet and Range according to the case.

Set RangeToFix = Sheets("outbreak").Range("B2:B201")

male_synonym = Array("M", "Masculino", "Masc", "Homem", "Man", "Male", "M.", "Masc.")
female_synonym = Array("F", "Feminino", "Fem", "Mulher", "Woman", "Female", "Fem.", "Wom.", "Femenino")

For Each Cell In RangeToFix
        If IsInArray(UCase(Cell.Value), Yes) Then
            Cell.Value = "M"
        Else
            If IsInArray(UCase(Cell.Value), No) Then
               Cell.Value = "F"
            End If
        End If
Next Cell
   
End Sub