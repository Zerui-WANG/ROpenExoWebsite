const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  entry: path.resolve(__dirname, "assets/src/index.js"),
  output: {
    filename: "bundle.js",
    path: path.resolve(__dirname, "assets/dist")
  },
    plugins: [
        new MiniCssExtractPlugin({
            filename: '[name].css',
            chunkFilename: '[id].css',
        })
    ],
    module: {
        rules: [{
            test: /\.scss$/,
            use: [
                MiniCssExtractPlugin.loader, // 3. Recrée les fichiers css à partir de leurs équivalents en Javascript.
                {
                  loader: 'css-loader'
                },
                {
                  loader: 'sass-loader',
                  options: {
                    sourceMap: true,
                    // options...
                  }
                }
            ],
            exclude: /node_modules/
        }]
    }
};