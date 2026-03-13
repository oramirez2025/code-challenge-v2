from rest_framework import serializers

from map.models import CommunityArea, RestaurantPermit


class CommunityAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityArea
        fields = ["name", "area_id", "num_permits"]

    num_permits = serializers.SerializerMethodField()

    def get_num_permits(self, obj):
        # In a given year, we want to find the number of permits for a community area
        # To do so, we'll filter out the RestaurantPermits with a given year and id? 
        """
        TODO: supplement each community area object with the number
        of permits issued in the given year.

        e.g. The endpoint /map-data/?year=2017 should return something like:
        [
            {
                "ROGERS PARK": {
                    area_id: 17,
                    num_permits: 2
                },
                "BEVERLY": {
                    area_id: 72,
                    num_permits: 2
                },
                ...
            }
        ]
        """
        year = self.context.get("year")
        community_area_id=obj.area_id
        qs = RestaurantPermit.objects.all()
        qs_filtered = qs.filter(community_area_id=community_area_id, issue_date__year=year)
        result = qs_filtered.count()

        return result
