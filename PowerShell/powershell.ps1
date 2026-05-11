#Error handling.
$ErrorActionPreference = "SilentlyContinue"
$Error.clear()

#Required parameters.
$apiKey = ""
$apiBase = ""
$model = ""

#Request setup.
$headers = @{
    "Authorization" = "Bearer $apiKey"
    "Content-Type"  = "application/json"
}

$body = @{
    model = $model
    input = "2+2"
} | ConvertTo-Json

#Submit the request.
$response = Invoke-RestMethod -Uri "$apiBase/responses" -Method Post -Headers $headers -Body $body
$response | ConvertTo-Json -Depth 5
