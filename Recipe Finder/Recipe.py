import requests


def search_recipes(api_key, query):
    base_url = "https://api.edamam.com/search"
    params = {
        "q": query,
        "app_id": "bb7528c5",
        "app_key": api_key,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        hits = data.get("hits", [])

        if not hits:
            print("No recipes found.")
        else:
            for hit in hits:
                recipe = hit.get("recipe", {})
                print("\nTitle:", recipe.get("label"))
                print("URL:", recipe.get("url"))
                print("Ingredients:", ", ".join(recipe.get("ingredientLines", [])))
                print("-" * 50)
    else:
        print("Error:", response.status_code)


if __name__ == "__main__":
    api_key = "2d8e542a11e73df2d74066ce268fab34"

    user_query = input("Enter a recipe search query: ")

    search_recipes(api_key, user_query)
