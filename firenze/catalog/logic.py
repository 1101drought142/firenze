class FormatedProduct():
    def __init__(
        self,
        id,
        name,
        photo_url,
        colors,
        materials,
        sizes,
        choosen_color,
        choosen_material,
        choosen_size,
        price, 
    ):
        self.id = id
        self.name = name
        self.photo_url = photo_url
        self.colors = colors
        self.materials = materials
        self.sizes = sizes
        self.price = price
        self.choosen_color = choosen_color
        self.choosen_material = choosen_material
        self.choosen_size = choosen_size

# По каждому продукту нужно 
class GetProductFormatted():

    def add_color(formated_product, variant_id, color):
        if not(formated_product.colors.get(variant_id)):
            formated_product.colors[variant_id] = color.color_code

    def add_material(formated_product, variant_id, material):
        if not(formated_product.materials.get(variant_id)):
            formated_product.materials[variant_id] = material.name

    def add_sizes(formated_product, variant_id, size):
        if not(formated_product.sizes.get(variant_id)):
            formated_product.sizes[variant_id] = size.name

    def set_choosen_variant(formated_product, variant):
        __class__.add_color(formated_product, variant.id, variant.color)
        __class__.add_material(formated_product, variant.id, variant.material)
        __class__.add_sizes(formated_product, variant.id, variant.size)

        formated_product.choosen_color = variant.color.color_code
        formated_product.choosen_material = variant.material.name
        formated_product.choosen_size = variant.size.name


    def get_product_json(product_query, choosen_variant=None):
        product = FormatedProduct(
            id = product_query.id,
            name = product_query.name,
            photo_url = product_query.photo.url,
            colors = {},
            materials = {},
            sizes = {},
            choosen_color = 0,
            choosen_material = 0,
            choosen_size = 0,
            price = 0
        )

        if choosen_variant:
            __class__.set_choosen_variant(product, choosen_variant)

        for product_type in product_query.producttype_set.all():
            
            if not(choosen_variant):
                choosen_variant = product_type
                __class__.set_choosen_variant(product, choosen_variant)

            __class__.add_color(product, product_type.id, product_type.color)
            __class__.add_material(product, product_type.id, product_type.material)
            __class__.add_sizes(product, product_type.id, product_type.size)
        return product
