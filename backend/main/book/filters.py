from django_filters import rest_framework as filters

from . import models


class BookFilter(filters.FilterSet):
    author = filters.CharFilter(method='author_name_search',)
    category = filters.CharFilter(method='category_title_search',)

    # def author_name_search(self, queryset, name, value):
    #     return self._filter_queryset(queryset, name, 'name', value)

    # def category_title_search(self, queryset, name, value):
    #     return self._filter_queryset(queryset, name, 'title', value)

    def author_name_search(self, queryset, name, value):
        return self._filter_queryset(queryset, name, 'id', value)

    def category_title_search(self, queryset, name, value):
        return self._filter_queryset(queryset, name, 'id', value)

    def _cleaned_params(self, value):
        try:
            raw_param = str(value).split(',')
            clean_param = [param for param in raw_param if isinstance(int(param), int)]
            return clean_param
        except Exception:
            raise

        # raw_param = value.split(',')
        # clean_param = [param for param in raw_param if param]
        # return clean_param

    def _filter_queryset(self, queryset, name, str_name,  value):
        try:
            lookup = '__'.join([name, str_name])
            for param in self._cleaned_params(value):
                queryset = queryset.filter(**{lookup:param})

                if not queryset:
                    break
            return queryset
        except Exception:
            return models.Book.objects.none()

        # lookup = '__'.join([name, str_name])
        # for param in self._cleaned_params(value):
        #     queryset = queryset.filter(**{lookup:param.strip()})

        #     if not queryset:
        #         break
        # return queryset

    class Meta:
        model = models.Book
        fields = [
            'author',
            'category',
        ]
