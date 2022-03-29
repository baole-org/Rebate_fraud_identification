# Styling
from datetime import timedelta
import pandas as pd

def highlight_cols(s):
    color = 'red'
    return 'background-color: %s' % color

def short_timedelta_highlight(s):    
  '''highlight the timedelta is less than 15 mins yellow.'''
  is_short = s<timedelta(minutes=30)
  return ['background-color: yellow' if v else '' for v in is_short]

def time_variance(sorted_time_column):
  '''This function takes a sorted column of datetime values, and return the minimum timedelta among them'''
  if sorted_time_column.shape[0] < 3:
    return None
  else:
    time_column_A = sorted_time_column[:-1].reset_index(drop=True)
    time_column_B = sorted_time_column[1:].reset_index(drop=True)
    time_diff = time_column_A - time_column_B
    return time_diff.min()