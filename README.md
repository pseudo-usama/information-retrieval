# Information retrieval

## How to run
First to install dependencies run this command:

    pip install numpy pandas streamlit

Now to run the project enter this command:

    streamlit run app.py

After that you'll see some ```localhost:PORT``` address in your terminal. Copy that and open it in a browser.

# IMPORTANT
To update the documents used in searching goto [default_docs.py](default_docs.py) and update a variable named ```DEFAULT_DOCS```.


## Files
 - [app.py](app.py) is the main entry point of this project. And it doesn't contain 
 - [search_docs.py](search_docs.py) contains all the code to calculate and search documents.
 - [default_docs.py](default_docs.py) contains the default documents used in searching.
