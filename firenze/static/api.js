class publicApi {

  constructor() {
    this.baseURL = '/api/v1';
  }

  addToCart = async (variantId) => {
    const res = await fetch(`${this.baseURL}/cart/add_to_cart`, {
      method: 'POST',
      body: JSON.stringify({
        variantId: +variantId
      })
    }).then(res => res.json())
    console.log(res, ' response');
    return res;

  }
  
  addToFavorites = async (productId) => {
    const res = await fetch(`${this.baseURL}/personal/add_to_favourites`, {
      method: 'POST',
      body: JSON.stringify({
        productId: +productId
      })
    }).then(res => res.json())
    console.log(res, ' response');
    return res;
  }
  deleteFromFavorites = async (productId) => {
    const res = await fetch(`${this.baseURL}/personal/delete_from_favourites`, {
      method: 'POST',
      body: JSON.stringify({
        productId: +productId
      })
    }).then(res => res.json())
    console.log(res, ' response');
    return res;
  }



  // account


  signUp = async (formData) => {
    const res = await fetch(`${this.baseURL}/personal/registration`, {
      method: 'POST',
      body: formData,
    }).then(res => res.json())
    console.log(res, ' response');
    return res;
  }


  // global

  search = async (string) => {
    const res = await fetch(`${this.baseURL}/catalog/search?query=${string}`)
    .then(res => res.text())
    return res;
  }

}

const PublicAPI = new publicApi();