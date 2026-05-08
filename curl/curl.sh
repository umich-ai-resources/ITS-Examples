#!/bin/bash
export API_KEY=""
export API_BASE=""
export API_MODEL=""

curl $API_BASE"/responses" \
-H "Content-Type: application/json" \
-H "Authorization: Bearer $API_KEY" \
-d "{
\"model\": \"$API_MODEL\",
\"input\": \"2+2=?\"
}"