
# Data Collection Options

## Structure

`Data Collection Options`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `title` | `str` | Required | The title text to display in the data collection flow on the Terminal.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `250` |
| `body` | `str` | Required | The body text to display under the title in the data collection screen flow on the<br>Terminal.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `10000` |
| `input_type` | [`str (Data Collection Options Input Type)`](../../doc/models/data-collection-options-input-type.md) | Required | Describes the input type of the data. |
| `collected_data` | [`Collected Data`](../../doc/models/collected-data.md) | Optional | - |

## Example (as JSON)

```json
{
  "title": "title4",
  "body": "body4",
  "input_type": "EMAIL",
  "collected_data": {
    "input_text": "input_text0"
  }
}
```

