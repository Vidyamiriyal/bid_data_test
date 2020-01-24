mouseColor=$(printf "%02x%02x%02x\n" $((RANDOM%256)) $((RANDOM%256)) $((RANDOM%256)))
ratbagctl warbling-mara led 0 set color $mouseColor
