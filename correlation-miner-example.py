import pm4py
import pandas as pd

df = pd.read_csv('correlation_mining.csv')
df = pm4py.format_dataframe(df, case_id = 'case:concept:name', activity_key = 'concept:name', timestamp_key='time:timestamp')
event_log = pm4py.convert_to_event_log(df)
type(event_log)