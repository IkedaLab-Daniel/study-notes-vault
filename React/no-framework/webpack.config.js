const path = require("node:path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const ReactServerWebpackPlugin = require("react-server-dom-webpack/plugin");
const plugin = require("react-server-dom-webpack/plugin");

const mode = process.env.NODE_ENV || "development";
const development = mode === "development";

const config = {
    mode,
    entry: "./src/Client.jsx",
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                use: "babel-loader",
                exclude: /node_modeules/,
            },
            {
                test: /\.css$/i,
                use: ["style-loader", "css-loader"],
            },
        ],
    },
    resolve: {
        extensions: [".js", ".jsx"],
    },
    plugin: {
        new HtmlWebpackPlugin({
            inject: true,
            publicPath: "/assets/",
            template: "./index.html"
        }),
        new ReactServerWebpackPlugin({ isServer: false }),
    },
    output: {
        chunkFilename: development ? "[id].chunk.js" : "[id].[contenthash].js"
    }
}