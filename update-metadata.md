# Just run it in cli
```bash
knife cookbook list | grep -E "$(grep -i "depends.*~>" metadata.rb | awk -F' ' '{printf"%s |", $2}' | tr -d \,\' | xargs echo)some" | awk -F '[[:space:]][[:space:]]+' '{print "depends '\''"$1"'\'', '\''~> "$2"'\''"}'
```
