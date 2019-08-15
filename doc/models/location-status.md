## Location Status

Indicates the location's status.

### Enumeration

`LocationStatus`

### Fields

| Name | Description |
|  --- | --- |
| `ACTIVE` | A fully operational location. The location can be used across all Square products and APIs. |
| `INACTIVE` | A functionally limited location. The location can only be used via Square APIs.<br><br>__NOTE__: We __strongly__ discourage the use of inactive locations.<br>Making API calls with inactive locations will cause complications<br>if the restrictions on inactive locations increase in the future. |

