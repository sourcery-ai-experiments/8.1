from __future__ import print_function

__all__ = ["ContactInfo", "PyUser", "User"]

from abc import ABCMeta, abstractmethod

from java.lang import Object


class ContactInfo(Object):
    def __init__(self, contactType=None, value=None):
        self.contactType = contactType
        self.value = value

    def getContactType(self):
        pass

    def getValue(self):
        pass

    def setContactType(self, contactType):
        pass

    def setValue(self, value):
        pass


class User(ABCMeta):
    _Badge = "badge"
    _DEFAULT_SCHEDULE_NAME = "Always"
    _FirstName = "John"
    _Language = "en"
    _LastName = "Doe"
    _Notes = "These are some notes."
    _Password = "password"
    _Schedule = "Always"
    _Username = "johdoe"
    _USERNAME_PATTERN = r"[\p{Alnum}][ @\w.\s\-]{1, 49}"

    def __new__(mcs, *args, **kwargs):
        print(args, kwargs)
        return super(User, mcs).__new__(mcs, mcs.__name__, mcs.__bases__, {})

    @property
    def Badge(cls):
        return cls._Badge

    @property
    def DEFAULT_SCHEDULE_NAME(cls):
        return cls._DEFAULT_SCHEDULE_NAME

    @property
    def FirstName(cls):
        return cls._FirstName

    @property
    def Language(cls):
        return cls._Language

    @property
    def LastName(cls):
        return cls._LastName

    @property
    def Notes(cls):
        return cls._Notes

    @property
    def Password(cls):
        return cls._Password

    @property
    def Schedule(cls):
        return cls._Schedule

    @property
    def Username(cls):
        return cls._Username

    @property
    def USERNAME_PATTERN(cls):
        return cls._USERNAME_PATTERN

    @abstractmethod
    def getContactInfo(cls):
        pass

    @abstractmethod
    def getId(cls):
        pass

    @abstractmethod
    def getPath(cls):
        pass

    @abstractmethod
    def getProfileName(cls):
        pass

    @abstractmethod
    def getRoles(cls):
        pass

    @abstractmethod
    def getScheduleAdjustments(cls):
        pass


class PyUser(User):
    """A User implementation that delegates to another user object, but
    has some methods that are more scripting friendly.
    """

    def __init__(cls):
        super(PyUser, cls).__init__(cls.__name__, cls.__bases__, {})

    def addContactInfo(cls, *args):
        """Convenience method for scripting to add a new contactInfo
        easily.

        Usage:
            1. addContactInfo(contactType: str, value: str)
            2. addContactInfo(dict: contactDictionary)

        Args:
            args: Variable length argument list.
        """
        print(cls, args)

    def addRole(cls, role):
        """Convenience method for scripting to add a new role easily.

        Only works if user type supports roles.

        Args:
            role (str): A new role to add. If empty or null, no
                effect.
        """
        print(cls, role)

    def addRoles(cls, roles):
        """Adds the provided roles to this user.

        Args:
            roles (list[str]): A list of roles.
        """
        print(cls, roles)

    def addScheduleAdjustment(cls, start, end, available=True, note=None):
        """Convenience method for scripting to add a new schedule
        adjustment easily.

        Args:
            start (Date): Date to start the schedule adjustment. Not
                null.
            end (Date): Date to end start the schedule adjustment.
                Not null.
            available (bool): True if the employee is available during
                this period. Optional.
            note (str): May be null or empty. Optional.
        """
        print(cls, start, end, available, note)

    def addScheduleAdjustments(cls, scheduleAdjustments):
        """Add Schedule Adjustments.

        Args:
            scheduleAdjustments (ScheduleAdjustment): ScheduleAdjustment
                object.
        """
        print(cls, scheduleAdjustments)

    def contains(cls, prop):
        """Returns if this users contains a given property."""
        pass

    def get(cls, propertyName):
        """Returns a the value of the requested item.

        Args:
            propertyName (str): The user property to retrieve.

        Returns:
            str: The value of the requested property.
        """
        print(cls)
        return propertyName

    def getContactInfo(cls):
        """Returns a sequence of ContactInfo objects.

        Each of these objects will have a contactType and value property
        representing the contact information, both strings.

        Returns:
            list[ContactInfo]: A sequence of ContactInfo objects.
        """
        ci_email = ContactInfo("email", "johdoe@mycompany.com")
        ci_phone = ContactInfo("phone", "+1 5551324567")
        ci_sms = ContactInfo("sms", "+1 5557654321")
        return [ci_email, ci_phone, ci_sms]

    def getCount(cls):
        """Get count."""
        print(cls)
        return 1

    def getId(cls):
        """An opaque identifier that can be used to identify this
        user.
        """
        pass

    def getOrDefault(cls, prop):
        """Returns a default value if the requested item is not
        present.

        Args:
            prop (Property): The user property to retrieve.

        Returns:
            object: The value of the requested property.
        """
        print(cls, prop)

    def getOrElse(cls, property, value):
        """Get the value for a given Property, or else fall back to
        value if it's not present.
        """
        pass

    def getPath(cls):
        """Generate an path that unambiguously references this user."""
        pass

    def getProfileName(cls):
        """The name of the user management profile this user was
        retrieved from.
        """
        pass

    def getProperties(cls):
        """Returns all properties for this user."""
        pass

    def getRoles(cls):
        """Returns all of the roles this user is a has."""
        return ["Administrator", "Developer"]

    def getScheduleAdjustments(cls):
        """Returns all of this user's upcoming schedule adjustments."""
        pass

    def getValues(cls):
        """Returns the opaque PropertyValue objects."""
        pass

    def isExtended(cls, prop):
        """Returns whether this property set contains a value for the
        prop, and the prop was actually inherited.
        """
        pass

    def isInherited(cls, prop):
        """Indicates whether the property was inherited from a parent
        type.
        """
        pass

    def iterator(cls):
        """Property iterator."""
        pass

    def merge(cls, other, localOnly):
        """Merges the values from other collection into this one."""
        pass

    def remove(cls, prop):
        """Remove a property for this user."""
        pass

    def removeContactInfo(cls, contactType, value):
        """Remove contact information for this user."""
        pass

    def removeRole(cls, role):
        """Remove a role for this user."""
        pass

    def removeScheduleAdjustment(cls, start, end, available=True, note=None):
        """Remove schedule adjustment for this user."""
        pass

    def set(cls, *args):
        """Set a property for this user."""
        pass

    def setContactInfo(cls, contactInfo):
        """Set contact information for this user."""
        pass

    def setRoles(cls, roles):
        """Set roles for this user."""
        pass

    def setScheduleAdjustments(cls, scheduleAdjustments):
        """Set schedule adjustments for this user."""
        pass
