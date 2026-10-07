import re
import secrets

from rest_framework import serializers

from applications.models import Application, QueueTicket

PHONE_RE = re.compile(r"^[0-9+\-\s()]{7,32}$")


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["id", "full_name", "phone", "product", "note", "status", "created_at"]
        read_only_fields = ["id", "status", "created_at"]

    def validate_full_name(self, value):
        cleaned = value.strip()
        if len(cleaned) < 2:
            raise serializers.ValidationError("Ad çox qısadır.")
        return cleaned

    def validate_phone(self, value):
        cleaned = value.strip()
        if not PHONE_RE.match(cleaned):
            raise serializers.ValidationError("Telefon nömrəsini yoxlayın.")
        return cleaned


class QueueTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueueTicket
        fields = ["id", "full_name", "phone", "branch_name", "service", "visit_date", "visit_time", "code", "created_at"]
        read_only_fields = ["id", "code", "created_at"]

    def validate_full_name(self, value):
        cleaned = value.strip()
        if len(cleaned) < 2:
            raise serializers.ValidationError("Ad çox qısadır.")
        return cleaned

    def validate_phone(self, value):
        cleaned = value.strip()
        if not PHONE_RE.match(cleaned):
            raise serializers.ValidationError("Telefon nömrəsini yoxlayın.")
        return cleaned

    def create(self, validated_data):
        for _ in range(8):
            code = f"Q{secrets.randbelow(9000) + 1000}"
            if not QueueTicket.objects.filter(code=code).exists():
                return QueueTicket.objects.create(code=code, **validated_data)
        raise serializers.ValidationError("Növbə kodu yaradılmadı.")
