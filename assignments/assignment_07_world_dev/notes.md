# Assignment 07

## Groupby

Two approaches: as_index=False vs reset_index()

- df8 = df7.groupby('Region', as_index=False)['value'].sum()
- df8 = df7.groupby('Region')['value'].sum().reset_index()
