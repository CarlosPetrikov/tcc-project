module.exports = {
    userDir: '/data',

    credentialSecret: "uninter-nodered-secret",

    uiPort: process.env.PORT || 1880,

    logging: {
        console: {
            level: "info",
            metrics: false,
            audit: false
        }
    },

    editorTheme: {
        page: { title: "Node-RED" },
        header: { title: "Node-RED" },
        login: { enabled: false },
        palette: { editable: true }
    }
};
