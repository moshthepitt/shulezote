from haystack import indexes
from schools.models import School


class SchoolIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    facts = indexes.MultiValueField(null=True)

    def prepare_facts(self, obj):
        return [fact.pk for fact in obj.facts()] or None

    def get_model(self):
        return School

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(active=True)

    def load_all_queryset(self):
        """Pull all objects related to the Product in search results."""
        return self.index_queryset().select_related()
