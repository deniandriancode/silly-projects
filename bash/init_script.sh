#!/usr/bin/env bash

# Create new file then make it executable
for i in ${@};
do
  echo "#!/usr/bin/env bash" > $i
  chmod +x $i
done
