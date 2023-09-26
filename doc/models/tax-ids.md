
# Tax Ids

Identifiers for the location used by various governments for tax purposes.

## Structure

`Tax Ids`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `eu_vat` | `str` | Optional | The EU VAT number for this location. For example, `IE3426675K`.<br>If the EU VAT number is present, it is well-formed and has been<br>validated with VIES, the VAT Information Exchange System. |
| `fr_siret` | `str` | Optional | The SIRET (Système d'Identification du Répertoire des Entreprises et de leurs Etablissements)<br>number is a 14-digit code issued by the French INSEE. For example, `39922799000021`. |
| `fr_naf` | `str` | Optional | The French government uses the NAF (Nomenclature des Activités Françaises) to display and<br>track economic statistical data. This is also called the APE (Activite Principale de l’Entreprise) code.<br>For example, `6910Z`. |
| `es_nif` | `str` | Optional | The NIF (Numero de Identificacion Fiscal) number is a nine-character tax identifier used in Spain.<br>If it is present, it has been validated. For example, `73628495A`. |
| `jp_qii` | `str` | Optional | The QII (Qualified Invoice Issuer) number is a 14-character tax identifier used in Japan.<br>For example, `T1234567890123`. |

## Example (as JSON)

```json
{
  "eu_vat": "eu_vat8",
  "fr_siret": "fr_siret0",
  "fr_naf": "fr_naf0",
  "es_nif": "es_nif4",
  "jp_qii": "jp_qii0"
}
```

