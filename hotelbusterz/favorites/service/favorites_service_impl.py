from favorites.repository.favorites_item_repository_impl import FavoritesItemRepositoryImpl
from favorites.repository.favorites_repository_impl import FavoritesRepositoryImpl
from favorites.service.favorites_service import FavoritesService
from product.repositiory.product_repository_impl import ProductRepositoryImpl


class FavoritesServiceImpl(FavoritesService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__favoritesRepository = FavoritesRepositoryImpl.getInstance()
            cls.__instance.__favoritesItemRepository = FavoritesItemRepositoryImpl.getInstance()
            cls.__instance.__productRepository = ProductRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def favoritesRegister(self, favoritesData, accountId):
        account = self.__accountRepository.findById(accountId)
        favorites = self.__favoritesRepository.findByAccount(account)

        print(f"account: {account}, favorites: {favorites}")

        if favorites is None:
            favorites = self.__favoritesRepository.register(account)

        productId = favoritesData.get('productId')
        print(f"productId: {productId}")
        favoritesItemList = self.__favoritesItemRepository.findAllByProductId(productId)
        print(f"favoritesItems: {favoritesItemList}")

        favoritesItem = None
        for item in favoritesItemList:
            favoritesFromFavoritesItem = item.favorites
            accountFromFavorites = favoritesFromFavoritesItem.account
            if accountFromFavorites.id == account.id:
                favoritesItem = item
                break

        if favoritesItem is None:
            product = self.__productRepository.findByProductId(favoritesData.get('productId'))
            self.__favoritesItemRepository.register(favoritesData, favorites, product)

