const { src, dest, watch, parallel } = require('gulp');

const sass = require('gulp-sass')(require('sass'));
const autoprefixer = require('gulp-autoprefixer');
const postcss = require('gulp-postcss');
const cssnano = require('cssnano');
// const rename = require('gulp-rename');
const imagemin = require('gulp-imagemin');
const cache = require('gulp-cache');
const notify = require('gulp-notify');
const sourcemaps = require('gulp-sourcemaps');
const webp = require('gulp-webp');
// const clean = require('gulp-clean');

const paths = {
    scss: 'src/scss/**/*.scss',
    // js: 'src/js/**/*.js',
    imagenes: 'src/resources/img/**/*'
};

function css() {
    return src( paths.scss )
        .pipe( sourcemaps.init() )
        .pipe( sass() )
        .pipe( postcss( [autoprefixer(), cssnano()] ) )
        .pipe( sourcemaps.write('.') )
        .pipe( dest('./build/css') );
};

function imagenes() {
    return src( paths.imagenes )
        .pipe( cache( imagemin( {optimizationLevel: 3} ) ) )
        .pipe( dest('build/img') )
        .pipe( notify( {message: 'Imagen Completa'} ) )
};

function versionWebp() {
    return src( paths.imagenes )
        .pipe( webp() )
        .pipe( dest('build/img') )
        .pipe ( notify( {message: 'Imagen Completada'} ) )
};

function watchArchivos() {
    watch( paths.scss, css );
    // watch( paths.js, javascript );
    watch ( paths.imagenes, imagenes ),
    watch( paths.imagenes, versionWebp );
};

exports.default = parallel( css, imagenes, versionWebp, watchArchivos );