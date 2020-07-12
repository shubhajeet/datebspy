REM Keep a global reference to the ScriptProvider, since this stuff may be called many times: 
Global g_MasterScriptProvider as Object
REM Specify location of Python script, providing cell functions: 
Const URL_Main as String = "vnd.sun.star.script:" 
Const URL_Args as String = "?language=Python&location=user" 

Function invokePyFunc(file AS String, func As String, args As Array, outIdxs As Array, outArgs As Array)
   sURL = URL_Main & file & ".py$" & func & URL_Args
   oMSP = getMasterScriptProvider()
   On Local Error GoTo ErrorHandler
      oScript = oMSP.getScript(sURL)
      invokePyFunc = oScript.invoke(args, outIdxs, outArgs)
      Exit Function
   ErrorHandler:
      Dim msg As String, toFix As String
      msg = Error$
      toFix = ""
      If 1 = Err AND InStr(Error$, "an error occurred during file opening") Then
         msg = "Couldn' open the script file."
         toFix = "Make sure the 'python' folder exists in the user's Scripts folder, and that the former contains " & file & ".py."
      End If
      MsgBox msg & chr(13) & toFix, 16, "Error " & Err & " calling " & func
end Function

Function getMasterScriptProvider() 
   if isNull(g_MasterScriptProvider) then 
      oMasterScriptProviderFactory = createUnoService("com.sun.star.script.provider.MasterScriptProviderFactory") 
      g_MasterScriptProvider = oMasterScriptProviderFactory.createScriptProvider("") 
   endif 
   getMasterScriptProvider = g_MasterScriptProvider
End Function

Function DateToAD(date)
    DateToAD = InvokePyFunc("custom_date","date_to_ad",Array(date),Array(),Array())
ENd Function

Function DateToBS(date)
    DateToAD = InvokePyFunc("custom_date","date_to_bs",Array(date),Array(),Array())
ENd Function