### A python script to pseudo-daemon ngrok tunnels and list the needed ip and ports

##### This script assumes a properly configured ngrok config at `~/.config/ngrok/ngrok.yml`. 
##### Here is an example config which creates two, for SSH and a Minecraft server:

  `version: "2"`
  `authtoken: foo`
  tunnels:
    app-one:
      addr: 22
      proto: tcp
    app-two:
      addr: 25565
      proto: tcp`

