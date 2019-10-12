var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
const ExtractTextPlugin = require("extract-text-webpack-plugin");

module.exports = {
    entry:  path.join(__dirname, 'assets/src/js/index'),

    output: {
        path: path.join(__dirname, 'assets/dist'),
        filename: '[name]-[hash].js'
    },

    module: {
        rules: [
            {
                test: /\.css$/,
                loader: ['style-loader', 'css-loader'],
            },
            {
                test: /\.jsx?$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
            },
        ],
    },

    plugins: [
        new BundleTracker({
            path: __dirname,
            filename: 'webpack-stats.json'
        }),
        new ExtractTextPlugin({
            filename: '[name]-[hash].css'
        }),
    ],
}