try:
  import Microsoft.Scripting.Silverlight
  Silverlight = True
except:
  Silverlight = False

import sys
sys.path.append("Lib")

if Silverlight:
  from System.Windows import Application
  from System.Windows.Controls import UserControl
  from Microsoft.Scripting.Silverlight import Repl

  sys.stdout = Repl.Current.OutputBuffer
  sys.stderr = Repl.Current.OutputBuffer

  Application.Current.RootVisual = UserControl()

import unittest
import test_sequence_functions

#suite = unittest.TestLoader().loadTestsFromTestCase(test_sequence_functions.TestSequenceFunctions)
#unittest.TextTestRunner(verbosity=2).run(suite)
unittest.main(test_sequence_functions)
