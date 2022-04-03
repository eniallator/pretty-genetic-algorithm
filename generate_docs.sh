rm -r docs
find docs-src -type f -exec dos2unix {} \;
../../docuowl-0.2.4/docuowl --input docs-src --output docs