mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"shah_dhru@bentley.edu\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml