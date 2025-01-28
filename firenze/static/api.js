class publicApi {

  constructor() {
    this.baseURL = '/api/v1';
    this.csrf = document.querySelector('#csrf input').value;
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
      headers: {
        "Content-Type": "application/json",
        'X-CSRFToken': this.csrf
      },
      body: JSON.stringify({
        variantId: +variantId,
        csrf: this.csrf,
      })
    }).then(res => res.json())
    return res;
  }

  removeFromCart = async (variantId) => {
    const res = await fetch(`${this.baseURL}/cart/delete_from_cart`, {
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
        'X-CSRFToken': this.csrf
      },
      body: JSON.stringify({
        variant_id: variantId,
        csrf: this.csrf,
      })
    }).then(res => res.text())
    return res; 
  }

  changeCartProductParam = async (productId, variantId) => {
    const res = await fetch(`${this.baseURL}/cart/change_cart_product_variant`, {
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
        'X-CSRFToken': this.csrf
      },
      body: JSON.stringify({
        variant_id: variantId,
        product_id: productId,
        csrf: this.csrf,
      })
    })
    .then(res => res.text());
    return res;
  }


  
  addToFavorites = async (productId, csrf) => {
    const res = await fetch(`${this.baseURL}/personal/add_to_favourites`, {
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
        'X-CSRFToken': this.csrf,
      },
      body: JSON.stringify({
        csrf: this.csrf,
        product_id: +productId,
      })
    }).then(res => res.json())
    console.log(res, ' response');
    return res;
  }
  deleteFromFavorites = async (productId) => {
    const res = await fetch(`${this.baseURL}/personal/delete_from_favourites`, {
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
        'X-CSRFToken': this.csrf,
      },
      body: JSON.stringify({
        product_id: +productId,
        csrf: this.csrf,
      })
    }).then(res => res.json())
    console.log(res, ' response');
    return res;
  }

  order = async (formData) => {
    const res = await fetch(`${this.baseURL}/order/order`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': this.csrf,
      },
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
      headers: {
        'X-CSRFToken': this.csrf,
      },
      body: formData,
    }).then(res => res.json())
    console.log(res, ' response');
    return res;
  }
  
  login = async (formData) => {
    const res = await fetch(`${this.baseURL}/personal/login`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': this.csrf,
      },
      body: formData,
    }).then(res => res.json())
    console.log(res, ' response');
    return res;
  }
  
  logout = async () => {
    const res = await fetch(`${this.baseURL}/personal/logout`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': this.csrf,
      },
    }).then(res => res.json())
    return res;
  }
  
  changeInfo = async (formData) => {
    console.log(formData);
    const res = await fetch(`${this.baseURL}/personal/change_info`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': this.csrf,
      },
      body: formData,
    }).then(res => res.json())
    return res;
  }
  
  forgotPass = async (formData) => {
    const res = await fetch(`${this.baseURL}/personal/request_password_change`, {
      method: 'POST',
      headers: {
        'X-CSRFToken': this.csrf,
      },
      body: formData,
    }).then(res => res.json())
    return res;
  }

  uploadPhoto = async (formData) => {
    const res = await fetch(`${this.baseURL}/personal/upload_file`, {
      method: 'POST',
      headers: {
        "Content-Type": "Multipart/form-data",
      },
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