class publicApi {

  constructor() {
    this.baseURL = '/api/v1';
  }

  
  // product

  changeProductParams = async (productId, variantId) => {
    const res = await fetch(`${this.baseURL}/catalog/change_product_param?product_id=${productId}&variant_id=${variantId}`)
    .then(res => res.text());
    return res;
  }

  addToCart = async (variantId) => {
    const res = await fetch(`${this.baseURL}/cart/add_to_cart`, {
      method: 'POST',
      body: JSON.stringify({
        variantId: +variantId
      })
    }).then(res => res.json())
    return res;
  }

  removeFromCart = async (variantId) => {
    const res = await fetch(`${this.baseURL}/cart/delete_from_cart`, {
      method: 'POST',
      body: JSON.stringify({
        variant_id: variantId,
      })
    }).then(res => res.json())
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

  order = async (formData) => {
    const res = await fetch(`${this.baseURL}/order/order`, {
      method: 'POST',
      body: formData,
    }).then(res => res.json())
    console.log(res, ' response');
    return res;
  }


  // catalog

  filter = async (formData) => {
    const str = new URLSearchParams(formData).toString();
    const res = await fetch(`${this.baseURL}/catalog/filter?${str}`)
    .then(res => res.text())
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
  
  login = async (formData) => {
    const res = await fetch(`${this.baseURL}/personal/registration`, {
      method: 'POST',
      body: formData,
    }).then(res => res.json())
    console.log(res, ' response');
    return res;
  }
  
  logout = async () => {
    const res = await fetch(`${this.baseURL}/personal/logout`, {
      method: 'POST',
    }).then(res => res.json())
    return res;
  }
  
  changeInfo = async (formData) => {
    const res = await fetch(`${this.baseURL}/personal/change_info`, {
      method: 'POST',
      body: formData,
    }).then(res => res.json())
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