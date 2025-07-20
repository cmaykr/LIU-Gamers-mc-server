# Configuration files
The configs for the mods should be put under the configs folder, when the server is started these configs will be copied over to each servers config folder. This way you can set your own default configuration for every mod.

# Server properties file
The default.properties file is the default properties file for every server and will be copied over to each server when they are created.
The port is changed automatically at server creation and they are used to communicate with the velocity proxy, they don't need to be port-forwarded or changed.


# Proxy
The proxy is used to allow for multiple servers running under the same port and address, players can switch between these servers freely and easily. The default port for the proxy is 25555 and needs to be port-forwarded if internet access is wanted.